---
date: 2026-05-06T00:26:00+00:00
series: 工程实践
updated: 2026-10-17T16:02:00+00:00
created: 2026-10-17T16:02:00+00:00
title: From MHA, MQA, GQA to MLA——Cache is all your need
id: 3fcb3b02-81c4-8118-9c2f-fe4cb1960400
---

# MHA[Multi-Head Attention]

The thinking behind the MHA is simple here:

Given an input sequence $X[x_1, x_2, ..., x_n]$，MHA is equal to the concatenation of multiple outputs from attention process.

$$
\begin{gathered}
O[o^{(1)}, o^{(2)}, ..., o^{(m)}] \\
o^{(h)} = Attn(q^{(h)}, k^{(h)}, v^{(h)}) \\
Attn = \frac{\sum_{i \le t} exp(q_t*k_i^T)v_i}{exp(q_t*k_i^T)}\\
h : head \\
t : the\ number\ of\ token \\
q = MLP_q(X) \\
k = MLP_k(X) \\
v = MLP_v(X) \\
 
\end{gathered}
$$

assume the output dimension is $d$, and the number of heads is $h$. Experimentally, we have the following equation: $d_k = d_v = d /h$. In the most of base cases, we only need to predict the t+1 word. and we can just cache the attention result, **KV Cache**, for our next use.

### Bottle Neck of the MHA

Me can easily find that the attention process becomes very expensive when the sequence becomes longer. We not only need to store the KV result, making more memory needs to be used for process. We also need to calculate the result of this long sequence. Even we have the most advanced GPU, communicating with multiple GPUs is very expensive for both training and inference jobs.

So, people start working on how to reduce the huge KV cache without loss the model performance.

# MQA[Multi-Query Attention]

MQA is quite intuitive that all heads share the same KV cache. The equation of MQA could be:

$$
\begin{gathered}
O[o^{(1)}, o^{(2)}, ..., o^{(m)}] \\
o^{(h)} = Attn(q, k, v^{(h)}) \\
Attn = \frac{\sum_{i \le t} exp(q_t*k_i^T)v_i}{exp(q_t*k_i^T)}\\
h : head \\
t : the\ number\ of\ token \\
q = MLP_q(X) \\
k = MLP_k(X) \\
v = MLP_v(X) \\
 
\end{gathered}
$$

Based on the equation, we can easily find that the method is quite aggressive that we directly use only one KV cache to do the job, losing the possibility that the model can more. But it is the most memory we can save from the KV cache side.

# GQA[Grouped-Query Attention]

GQA is rather a kind of trade off when we look at the MHA and the MQA. It first group the heads and heads in the same group share the KV cache. We can use the following equation to model the method

$$
\begin{gathered}
O[o^{(1)}, o^{(2)}, ..., o^{(m)}] \\
o^{(h)} = Attn(q^{(g)}, k^{(g)}, v^{(h)}) \\
Attn = \frac{\sum_{i \le t} exp(q_t*k_i^T)v_i}{\sum_{i \le t}exp(q_t*k_i^T)}\\
g : group \\
h : head \\
t : the\ number\ of\ token \\
q = MLP_q(X) \\
k = MLP_k(X) \\
v = MLP_v(X) \\
 
\end{gathered}
$$

# MLA [Multi-Head Latent Attention]

Deepseek team proposed this method in their deepseek v2 paper, and they said the method is inspired by **Low-rank approximation.** In this part of the page, we’re going to have a close look on the MLA.

## Part 1

we first look back to the GQA method. In GQA method, the input $X$ will be first separated equally, generating two $K,V$ pairs. These pairs, will be separated equally into $G$ groups and copied $h/g$ times. In MLA, there is a little difference from GQA. Instead of separate the input, MLA choose first project the input into $C$ space, then do the attention. The whole process could be formulated as the following equation:

$$
\begin{gathered}
O[o^{(1)}, o^{(2)}, ..., o^{(m)}] \\
o^{(h)} = Attn(q^{(h)}, k^{(h)}, v^{(h)}) \\
Attn = \frac{\sum_{i \le t} exp(q_t*k_i^T)v_i}{\sum_{i \le t}exp(q_t*k_i^T)}\\
h : head \\
t : the\ number\ of\ token \\
c = MLP_c(X) \\
q = MLP_q(X) \\
k = MLP_k(C) \\
v = MLP_v(C) \\
 
\end{gathered}
$$

Wait, it seems not right that by introducing the C space that the KV cache is still needed.

We look back to the equation of the Dot-Attention:

$$
q_{t}^{(s)}k_{i}^{(s)} = (x_{t}W_q^{(s)})(c_{i}W_k^{(s)})^T = x_{t}(W_q^{(s)}W_k^{(s)T})c_i^T
$$

Which means, when the model is in inference mode, we can cache the product of $W_q^{(s)}W_k^{(s)T}$. Based on the same meaning, we can find that there is another projection matrix after the $o^s$, named as $W_{proj}$, and also the $v_i^{s} = c_iW_i^{s}$, which means that we can also cache the product of $W_i^{s}W_{proj}$.

It can be easily observed that by caching the product result of these matrix, all the attention head share the same $c$ value. Which means the MLA, when inferencing, becomes a MQA.

### append

1. The merge of the matrix product like $W_q^{(s)}W_k^{(s)T}$only works when the precising is infinity. When we use it in BF16, the error share be observable and accumulated in the network.
2. In practice, we keep the original computing procedure for the computing source requires lower in the low rank and the precision loss the smaller.

## Part 2

The drawback for the current method is the MLA does not fit in RoPE.

Given:

$$
\begin{gathered}
q_i^{(s)} = x_iW_q^{(s)}R_i,\ k_i^{s} = c_iW_k^{(s)}R_i \\
q_t^{(s)}k_i^{sT} = x_t(W_q^{(s)}R_tR_i^TW_k^{(s)T})c_i^T = x_t(W_q^{(s)}R_{t-i}W_k^{(s)T})c_i^T
\end{gathered}
$$

As the value of $R_{t-i}$ position related, we cannot just cache the result of $W_q^{(s)}W_k^{(s)T}$.

DeepSeek Team use an appended dimension to fit in RoPE. They add $d_r$ dimensions to Q and K for RoPE, and K share the dimension with each head.

So, in mathematically, we can formulate the method in following equations.

$$
\begin{gathered}
o_t = [o_1, o_2, o_3, ..., o_h] \\
o_t^{s} = Attention(q_t^s, k_{i \le t}^s, v_{i \le t}^s) = \frac{\sum_{i \le t} exp(q_t^s*k_i^{sT})v_i^s}{\sum_{i \le t}exp(q_t^s*k_i^{sT})}\\
q_i^{(s)} = [x_iW_{qc}^{(s)}, x_iW_{qr}^{(s)}R_i], W_{qc} \in \mathbb R^{d*d_k}, W_{qr} \in \mathbb R^{d*d_r}\\

k_i^{(s)} = [c_iW_{kc}^{(s)}, x_iW_{kr}^{\sout {(s)}}R_i], W_{kc} \in \mathbb R^{d*d_k}, W_{kr} \in \mathbb R^{d*d_r}\\
v_i^{(s)} = c_iW_v^{(s)}, W_v \in \mathbb R^{d_c * d_v} \\
c_i = x_i W_c, W_c \in \mathbb R^{d*d_c}
\end{gathered}
$$

By doing so, those dimensions do not have rope information can just repeat the operation in Part 1, caching the result of $W_q^{(s)}W_k^{(s)T}$. And for those dimension who has the RoPE information, they can be done using the conviction method.

Also, because of the RoPE information is shared cross the head, for K cache there is only $d_r$ dimension is added.

### Part 3

One and the final modification is that the DeepSeek team apply Lowrank approximation method on Q

$$
\begin{gathered}
o_t = [o_1, o_2, o_3, ..., o_h] \\
o_t^{s} = Attention(q_t^s, k_{i \le t}^s, v_{i \le t}^s) = \frac{\sum_{i \le t} exp(q_t^s*k_i^{sT})v_i^s}{\sum_{i \le t}exp(q_t^s*k_i^{sT})}\\

q_i^{(s)} = [c'_iW_{qc}^{(s)}, c'_iW_{qr}^{(s)}R_i], W_{qc} \in \mathbb R^{d'_c*d_k}, W_{qr} \in \mathbb R^{d'_c*d_r}\\

k_i^{(s)} = [c_iW_{kc}^{(s)}, x_iW_{kr}^{\sout {(s)}}R_i], W_{kc} \in \mathbb R^{d'_c*d_k}, W_{kr}^{\sout {(s)}} \in \mathbb R^{d'_c*d_r}\\

v_i^{(s)} = c_iW_v^{(s)}, W_v \in \mathbb R^{d_c * d_v} \\
c'_i = x_i W_c', W_c' \in \mathbb R^{d *d_c'} \\
c_i = x_i W_c, W_c \in \mathbb R^{d*d_c}
\end{gathered}
$$

LOOK AT the 2nd part of the $k_i^{(s)}$, the part with RoPE, the input is still the $x_i$. $d’ = 1536$ in the original paper, which is different from $d_c = 512$.

When compared with the original MHA with RoPE, we can find that there is no big difference between them in training mode except **only some dimension has RoPE in MLA while all dimension has RoPE in MHA**.

In the inference mode, MLA goes to the MQA fashion that some dimension on K and V are shared cross the heads.
