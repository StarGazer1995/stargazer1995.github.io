---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RY5SCVYT%2F20260615%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260615T095137Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCpsJKymUrKZyLVgNxGVwW85KCuDIMPZ%2BHzFgowTzVRIgIgQ8K56BYfKFfHrCOBCev7v4%2BuUBm0JrdKjc9P5rUXQnEq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDOqUZlukNpsYn6Do0yrcA%2B3bB2xKbzaEWrpWj85Kxuxm4JrWkia2SHq4ow4sa8MyJuz2wPsMNrJhQsbD1dbgOuRges3bJzdjvjpbnfXFiOPbStDpXOie%2FjBcfssuhYVnRvAQ%2B8mwBe8306LkwuhZDj84cSzsZlDaohjxnL7IM9oLmBQvXB2Z%2BX0P1n3HwouIF1rExo%2Bm2StM5nwIKZRxI%2BuCAGrd5%2FcBDucHh95jDdTPAEkaAIo4UwiS%2BgToGESSFM3P6fZZOVtbP43AJYs2RJ%2BJuZfXikyATJvWwOT0ro53BWcJzhcAHO%2BUuMMXPbYZB%2FYhnCncGjq%2BzMJhscJw801tultkhCim8Sxa%2FG5HlAlhtJYkJS45tJrZFBJLt%2FirL0I0WhLJXNnTVCGzuZQibzRctk0dN5Nu8IvWHtJsNrUrzx1jlJ3tsdna%2BiXxhOxIKgbttpiwcxPqydAWyQmqB5l2ZdTIMbJ%2BQqi5NgzWMsBmrwTzHfHwir4RwBPBE9jopRrDG87OXMe7aSt%2FT8E%2BdtLTarOPGPGVKy3VTG72DtDtJUSUuxWBpJvNaFXtufCcmCdiwPDSkkKEUkeJr%2BzSOOUDEjPMJuiPBtxlCniIX8C65ALJFYOJowBb9eavUrvqjB0uPHDGVAkuLvgxMLn1vtEGOqUBtCqnVaOQENpFDdEmoG%2F%2BNisyhBf0AOk4c4LCYsjcc3BTltH6jEi3xlC4XGu%2FIo3ud9vSsx6H6jMvD2X%2FIhiP8R%2Bio3Rb3GnsLwFE2xLGcT5yr6pbfvPOW4KxI7oOnk%2BIt9RUoC%2F2s7OT0iiALRas6tZwIEfiRzxNZ2VdGW%2Bdt6X6pixzobLYNS9us5wgVeAKkRxzd7tKNIPPeqXuUFrSzNzJdi4b&X-Amz-Signature=d75a4e4a84438672e710dc0c162195fc6f104336f77d1304ce2103cd63826adc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
