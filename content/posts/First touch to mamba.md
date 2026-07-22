---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46626PCZXQU%2F20260722%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260722T185503Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJIMEYCIQCydY7Er6kBBMVckDAYwQfCfZLpGmUgXGBp8fKePX%2FY7AIhALvD9qrRX%2FTMUzSlGWKKdrnM9ItyJeUWGuYYb1AkMRksKogECNr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxjpGXHARUfQuamYakq3ANpnn8laHQ7shYMW%2BmR9UkpTHBY7xgtrhttT321pmudL%2BqZjyK4QhBiWmv450j9gewaDMjFsX8bbLZirWAhgTJYtOme2%2F7zWYyQgQnnKCEdyVw%2BpVi27qtdHteEUMaadM%2FqdDFKcC2CLJjK6Z3geEsPMk3OxEZLqLy4oME7n7LrrAODeV%2FfTwZCMQfxoVW%2FRcOEmFA6x%2FxmKlZve8ZgXQi8%2FpojZsW%2B3Y%2FowOy8uqaGezDSPGHCh7fu69mAmPKBhT%2FwGk4zeZFmrUfbMOkywR910k0K8t3QjT0KfRiWlvJwannNytvSp%2BloU2%2BEvi8n5TLezO77i1Y0EJKDTh7c5OrVMSqRg1AZf8S%2FRZYBi4DBkAtEMMy6Hjyxuv3LQ2ezYO5Z2Y09V3gJ8RzO9DwJvlRWb53lPtET7XGqtKTSO%2FDaTbzPTOqVbTmieuIO8KB2Jk7UA4f57PhzdER0ChG0jDu0ZIjr1Lvx0rOERO3Jpfu%2FM4EEkStySgrPHYpdmGQErgV7CVbVF3ugX2Z9Jr0QXFvU3KF7quK7pmoCKYqhzqWDWxTwFUZ9GTH2V8JutDhIbU0wg052EBJsj9Cc%2BgftIG%2Ff7hIbupBM5Kn%2FXGmyW5Q6QRgIV2KRoIBDnuwTqDCy74PTBjqkAaEYc9is9zL26bCR4HUPHwmZrbgO5QRi3d9uNryereCvahh1tMffAqwsMOdnJ28jKfDTRlKq%2FdBzh1izhFd60C784qudG8%2BxNLzAtNP53GPiq362jLXheifAgAuQEzQVGSQalYd4B%2BWRLXVG1%2Bd2uh9cqc7E1gU20kgl6AfQT5bNrj1GTTJZI7SeFmay41PSttnZ0kQ%2F5nj6EJlcNJ3D6lsoGtIK&X-Amz-Signature=ac06072396b8c86bf1f1c36ec498073346ae1ca51309c43806d51b0c34cd456b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
