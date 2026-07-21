---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y7ZKMYJH%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T114157Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCAdSYuUCnpfRJ3MC6TvQeVeBKGUwl4MZoPY%2B6xaQQWVgIgfeymhuBlD4RjwXNl89ahLGwEmZVj9A9fiaQcwiVyfTcqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMETpWfYqwjWMPsP%2ByrcA0QmV23Agrst1PRid1b695QmhNI1z%2BtGkInhMyedlRZqawIMKaJDRJ4jO0m0q4JQy4awVcaDZIJ4TR47X60Nlp0ANVEo9%2BGN2egoRZrShb50WcD5piITbJ6D2b9oKwDyOs%2BwZ3mmUbwhpKMdEWHty2yfjJYSUDxCas2l6PhN%2FfBSn2aiiD2FaW9IveWD1gLaaPeZYB1fJ6PzNQBkfMpDnUeQ9XYrxFXVnHBsXylm4sMZMrSoBN2BawwWqrxDhzURm6DSDyOXWTTexrLVpR%2Bgho94TlaoLZZrCT78rLZYx2VBapnK5C%2BJHs%2FtajrqG0Pb%2Fz4%2BZw66diUv23eElfa1qfJXqHXlYz6nmWPFrA6pMRL7PkbXJs4%2BhxXl33rDWHvIFVCGIZ%2BTUa%2BAlTI7tzsiG8Sfl6S8uruQgfwBxm9kiu0uE5jtW7Gk1TIcNnwV71%2B3ptsTA1yBSW5aCxp9iFR9TwBJBswo2JU2YriV1k1YGDc%2Bj%2BxDX5s8dOkgluKaKypWITbC6P3U8Gtf661XTtwL4yxYQa2Y4GvWvZWzVF72wAAkKaIEDK0V7Sn2OD1cDCtfSZcuk2VVVgnbo54vcEIAsKHWVvKApgL76qFdrnjf0gIV1L%2FiOtf5fE5ROPbIMIWQ%2FdIGOqUBzZW%2F3m64vWbzA0PemR5zJD72%2FF9Q5XWxn48SowKR349zA5o9JzPcONa067X3ZRz90q%2BNGQ7FTVweJkqE2IFClf4oncuT3HFI4jKZVfC5M766vbZknnPI0kc449%2FIdjkVfTM%2BkDrvuw6I2YQ%2FYa7nrFm7%2Fjfh0FUGDspk3LspLWGQJ%2Fz6BjodxuR%2Btf87zbKu2xUYncYvAv2pwYtfX3QIMjoCVPqz&X-Amz-Signature=8d009305c36a2c21966a8e8e3542c8a1ec159dbfee093dd2c0b05dc89488459e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
