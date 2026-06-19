---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46674WDIOHI%2F20260619%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260619T024648Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCNabpZO1NQ2Qj62Y4wAaYN0NPDSFYJtRy2z3xd2rrdxQIhANxElB3eNpJIjc2IalSW%2FhxfslHdPWFKqFKzEEa%2FayluKogECLL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyySQwCVgBgcp6c0%2Boq3APn1TOHmjVtUyCncYmpyLcojbpc1Xe9ex7qqZV5AtDdcn2tMC%2Fh18%2B4b1mgssfPNEsK%2FSZ1jpYSQ7FK9dMHum9JFj%2B4cvORn%2Frt2tQgZT5rXLe39fKGeUPBxPuuM3VH%2FUZ0PlI9ECFYHDyUELZAEzZ%2F9yb38xTVEBOGiNR%2F8%2BJKQaDRWhcTixN6Nd4%2BVpJ%2B9yyMbywTB39pqnvavdCIjLg1Lho3RfjVDWx%2FOPYE01Z%2BZWPPwEi9heFtibZUPh8P85Dp61JAJLERdf8le7QNcN%2FPnHykN0DCAhhqjLpji1U%2BdyN2yKYxNU%2FqS1ysRuADQZE7D3msYvzkKsjmLWCKrV%2BfqSbFByHy4FIM7PgzPRQLR6bWeSziTxe76Bn%2FH9%2BhNvNONGSxhM%2BUYWtZE6pKNO0YlrJXccyizz69mwHgp1neGdYErBRloouGxwqtI%2FZZaeRyLOxmZOm70dXis8G2tPs7k9%2FMYOm8X5R%2FGk60yk808KB9HmAbZotXloAR2A9h5H0F9hdN%2F8xAQr4CHUIjXLWk8Dbbz05ZRSMwowH7GBiRWf8LVdCLGfy6k0cVNHUHuKosijTlguv7ui45ZYiqJtVghAwIRCobiYpZsWbaswU8a03SXsJMfqM66c69VTDfoNLRBjqkAW722X4nBqIpDtfn7bZcsfopZyQM12UnSDlYS1eOk5jMFbWid%2B9xj3oWkyI5jS7KVFsMkbBCrvt09zlM3MmGmDomWrJgpf965ushMZL1bifsXUQ9w2cgL%2BKdZhGRrPLS1B7LOxDDXchiTm4aJKnr1BzRram5kAnj7Mz%2B8izTzkZDCj9LVVOB3%2FvXp6vxSNMWgxtx4iSNnInQR8OiFxv%2FxHXKtTLZ&X-Amz-Signature=496d721a0e9011b9665bba5c3920a09a091d3579c2adeb52d674726047131bcf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

From the perceptive of the structure of mamba, this is a discrete selective space machine that runs in linear time using linear space.

lets say, matrix A is a state space matrix for the last system status h(t). we then can calculate the next h(t+1) based on the following equation:

$$
\begin{equation}h(t) = A*h(t-1) + B*x(t)\end{equation}
$$

$$
y = C*h(t)
$$

Where B is a weight for input x(t) and C is the weight for output y.

We define A matrix in a HiPPO matrix manner.

$$
A = \begin{cases} \sqrt{(2n+1)(2k+1)} && everything-below -diagonal \\
n+1 && on-diagonal \\
0 && everything-beyond-diagonal \end{cases}
$$

By doing this, we can use SVD partition for reducing the computing demand.

$$
A=V\Lambda V^* - PQ^T = V(\Lambda - (V^*P)(V^*Q)^*)V
$$

This can be done
