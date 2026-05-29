---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YNYSFYMB%2F20260529%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260529T111854Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDs7KxI2CMjltBnpbp5zpvPj5X%2Bq1lpTt%2FxoNKqkP2%2BVAIgQ3wMSmVJL5S%2B4YPPbCY0lqfE%2FeGuVZ%2BDRp3b%2F13OOLEqiAQIxP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC6XWE8MtOOrC6CRKyrcA645%2FEZb7vUM64cldfBzAzMFo33QP1aNoA9Q2UikMvtRINQcr0sf5U4O6T%2F1IbUAPAWODPK%2B1HAlU2PTpETGq1TMunJ2CfTW5EPSZt78XCEk99v1%2F0xR1zf9LEGx7%2BzvYmIjCPQudqz8GVppx94fxFTg3JEzjA98%2BTL1FxeXh8BMUBFOTB6WrqVaYpWqN3M5wl%2FFXVpnbFUAFhE0YN9uQMDIGslZsC6eqxgGddqMOqs0A%2Ba0mI9duFPGanyA%2Bjpt8dzVHUXBpVpDDkPryGiwAIx7mT%2BM67qSJEyoER5SjKFHFHLbCC1Vz5dN9jqrmdQFu%2F7QOwyhxcSBNI3ok5px%2B9%2BB75huY%2F3gtBsSFR1KRztwze5PAVDPGrrO07AbS3GGRqzlHGI1HpJy22dEiLTGBatfZY2C8xOXTMcnqS5E9K5jYrFh809Yfwl9vZmfj6EhWqyuc6jMZ6DJVgBWHOlFVcwpEmpQw8zcMwzXu1YGfAXHwni%2FkaOLtB8FD%2FkpAFhEUIsbO3rY3Zcle0a9LqxAsmAzvL2VitOdqujRSdxQ%2BF62CGy%2BPH5c7CwUP4XngsG0rcEwAjU937x0l4vmOKOyxZPJ0afafCmi9e3r9IEoM4zcO%2BTG0Q2i0YMcxbghMOze5dAGOqUBDY2CA21LJCzmld%2FKjDYQpfAdjZj%2FuosogVSxX%2BnBLnKG73tXusiRJUke1ZxPEJ%2BKfXEeD9hCOwLiiJO2TrBMwEr58gbFQfe0AFsLkOOfZ%2FAmh%2By5gxbbqH92ZQfNvRgUO1KMVc5SfmD3eJAEOOwxBnDN37Z%2BuX3GhcoKWvdEkBXZwj5gCI22bqpN9Ryo5lyQns3it138EMxNyX0TIiBqgQP9RXOr&X-Amz-Signature=2d9444ea50a4d118941a406d7b29aca8cb130688a59051eb889c4f7fadcfc25e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
