---
created: 2026-05-06T00:26:00+00:00
updated: 2026-05-06T00:31:00+00:00
date: 2026-05-06T00:26:00+00:00
title: From MHA, MQA, GQA to MLA——Cache is all your need
id: 358b3b02-81c4-8163-a044-cd08783e4845
---

# MHA[Multi-Head Attention]

The thinking behind the MHA is simple here:

Given an input sequence ，MHA is equal to the concatenation of multiple outputs from attention process.

$$
O[o^{(1)}, o^{(2)}, ..., o^{(m)}] \newline
o^{(h)} = Attn(q^{(h)}, k^{(h)}, v^{(h)}) \newline
Attn = \frac{\sum_{i \le t} exp(q_t*k_i^T)v_i}{exp(q_t*k_i^T)}\newline
h : head \newline
t : the\ number\ of\ token \newline
q = MLP_q(X) \newline
k = MLP_k(X) \newline
v = MLP_v(X) \newline
 \newline
$$

assume the output dimension is , and the number of heads is . Experimentally, we have the following equation: . In the most of base cases, we only need to predict the t+1 word. and we can just cache the attention result, **KV Cache**, for our next use.

### Bottle Neck of the MHA

Me can easily find that the attention process becomes very expensive when the sequence becomes longer. We not only need to store the KV result, making more memory needs to be used for process. We also need to calculate the result of this long sequence. Even we have the most advanced GPU, communicating with multiple GPUs is very expensive for both training and inference jobs.

So, people start working on how to reduce the huge KV cache without loss the model performance.

# MQA[Multi-Query Attention]

MQA is quite intuitive that all heads share the same KV cache. The equation of MQA could be:

$$
O[o^{(1)}, o^{(2)}, ..., o^{(m)}] \newline
o^{(h)} = Attn(q, k, v^{(h)}) \newline
Attn = \frac{\sum_{i \le t} exp(q_t*k_i^T)v_i}{exp(q_t*k_i^T)}\newline
h : head \newline
t : the\ number\ of\ token \newline
q = MLP_q(X) \newline
k = MLP_k(X) \newline
v = MLP_v(X) \newline
 \newline
$$

Based on the equation, we can easily find that the method is quite aggressive that we directly use only one KV cache to do the job, losing the possibility that the model can more. But it is the most memory we can save from the KV cache side.

# GQA[Grouped-Query Attention]

GQA is rather a kind of trade off when we look at the MHA and the MQA. It first group the heads and heads in the same group share the KV cache. We can use the following equation to model the method

$$
O[o^{(1)}, o^{(2)}, ..., o^{(m)}] \newline
o^{(h)} = Attn(q^{(g)}, k^{(g)}, v^{(h)}) \newline
Attn = \frac{\sum_{i \le t} exp(q_t*k_i^T)v_i}{\sum_{i \le t}exp(q_t*k_i^T)}\newline
g : group \newline
h : head \newline
t : the\ number\ of\ token \newline
q = MLP_q(X) \newline
k = MLP_k(X) \newline
v = MLP_v(X) \newline
 \newline
$$

# MLA [Multi-Head Latent Attention]

Deepseek team proposed this method in their deepseek v2 paper, and they said the method is inspired by **Low-rank approximation.** In this part of the page, we’re going to have a close look on the MLA.

## Part 1

we first look back to the GQA method. In GQA method, the input will be first separated equally, generating two pairs. These pairs, will be separated equally into groups and copied times. In MLA, there is a little difference from GQA. Instead of separate the input, MLA choose first project the input into space, then do the attention. The whole process could be formulated as the following equation:

$$
O[o^{(1)}, o^{(2)}, ..., o^{(m)}] \newline
o^{(h)} = Attn(q^{(h)}, k^{(h)}, v^{(h)}) \newline
Attn = \frac{\sum_{i \le t} exp(q_t*k_i^T)v_i}{\sum_{i \le t}exp(q_t*k_i^T)}\newline
h : head \newline
t : the\ number\ of\ token \newline
c = MLP_c(X) \newline
q = MLP_q(X) \newline
k = MLP_k(C) \newline
v = MLP_v(C) \newline
 \newline
$$

Wait, it seems not right that by introducing the C space that the KV cache is still needed.

We look back to the equation of the Dot-Attention:

$$
q_{t}^{(s)}k_{i}^{(s)} = (x_{t}W_q^{(s)})(c_{i}W_k^{(s)})^T = x_{t}(W_q^{(s)}W_k^{(s)T})c_i^T
$$

Which means, when the model is in inference mode, we can cache the product of . Based on the same meaning, we can find that there is another projection matrix after the , named as , and also the , which means that we can also cache the product of .

It can be easily observed that by caching the product result of these matrix, all the attention head share the same value. Which means the MLA, when inferencing, becomes a MQA.

### append

1. The merge of the matrix product like only works when the precising is infinity. When we use it in BF16, the error share be observable and accumulated in the network.
2. In practice, we keep the original computing procedure for the computing source requires lower in the low rank and the precision loss the smaller.

## Part 2

The drawback for the current method is the MLA does not fit in RoPE.

Given:

$$
q_i^{(s)} = x_iW_q^{(s)}R_i,\ k_i^{s} = c_iW_k^{(s)}R_i \newline
q_t^{(s)}k_i^{sT} = x_t(W_q^{(s)}R_tR_i^TW_k^{(s)T})c_i^T = x_t(W_q^{(s)}R_{t-i}W_k^{(s)T})c_i^T
$$

As the value of position related, we cannot just cache the result of .

DeepSeek Team use an appended dimension to fit in RoPE. They add dimensions to Q and K for RoPE, and K share the dimension with each head.

So, in mathematically, we can formulate the method in following equations.

$$
o_t = [o_1, o_2, o_3, ..., o_h] \newline
o_t^{s} = Attention(q_t^s, k_{i \le t}^s, v_{i \le t}^s) = \frac{\sum_{i \le t} exp(q_t^s*k_i^{sT})v_i^s}{\sum_{i \le t}exp(q_t^s*k_i^{sT})}\newline
q_i^{(s)} = [x_iW_{qc}^{(s)}, x_iW_{qr}^{(s)}R_i], W_{qc} \in \mathbb R^{d*d_k}, W_{qr} \in \mathbb R^{d*d_r}\newline

k_i^{(s)} = [c_iW_{kc}^{(s)}, x_iW_{kr}^{\sout {(s)}}R_i], W_{kc} \in \mathbb R^{d*d_k}, W_{kr} \in \mathbb R^{d*d_r}\newline
v_i^{(s)} = c_iW_v^{(s)}, W_v \in \mathbb R^{d_c * d_v} \newline
c_i = x_i W_c, W_c \in \mathbb R^{d*d_c}
$$

By doing so, those dimensions do not have rope information can just repeat the operation in Part 1, caching the result of . And for those dimension who has the RoPE information, they can be done using the conviction method.

Also, because of the RoPE information is shared cross the head, for K cache there is only dimension is added.

### Part 3

One and the final modification is that the DeepSeek team apply Lowrank approximation method on Q

$$
o_t = [o_1, o_2, o_3, ..., o_h] \newline
o_t^{s} = Attention(q_t^s, k_{i \le t}^s, v_{i \le t}^s) = \frac{\sum_{i \le t} exp(q_t^s*k_i^{sT})v_i^s}{\sum_{i \le t}exp(q_t^s*k_i^{sT})}\newline

q_i^{(s)} = [c'_iW_{qc}^{(s)}, c'_iW_{qr}^{(s)}R_i], W_{qc} \in \mathbb R^{d'_c*d_k}, W_{qr} \in \mathbb R^{d'_c*d_r}\newline

k_i^{(s)} = [c_iW_{kc}^{(s)}, x_iW_{kr}^{\sout {(s)}}R_i], W_{kc} \in \mathbb R^{d'_c*d_k}, W_{kr}^{\sout {(s)}} \in \mathbb R^{d'_c*d_r}\newline

v_i^{(s)} = c_iW_v^{(s)}, W_v \in \mathbb R^{d_c * d_v} \newline
c'_i = x_i W_c', W_c' \in \mathbb R^{d *d_c'} \newline
c_i = x_i W_c, W_c \in \mathbb R^{d*d_c}
$$

LOOK AT the 2nd part of the , the part with RoPE, the input is still the . in the original paper, which is different from .

When compared with the original MHA with RoPE, we can find that there is no big difference between them in training mode except **only some dimension has RoPE in MLA while all dimension has RoPE in MHA**.

In the inference mode, MLA goes to the MQA fashion that some dimension on K and V are shared cross the heads.
