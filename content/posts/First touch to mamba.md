---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X42DUMFG%2F20260620%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260620T190739Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJIMEYCIQC3MfbrBu5bMUW9G9eQr2zxUdGe3v7OUMr0UIxXFp4aQAIhAIiGqKHgXSFWm%2BYH0J30rokfcgotaous3YjYhYZAScDrKogECNz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxfyAc0SDY9qa3X72gq3APbetnlFiwTklRmd2ezGniu3w1fPUoecFCAe2304H%2FB0S2JODo0VDdItMayTUrXTbHAkS2GOHu9OChuDziF7ilYayh6g3WC94IhJfHrrIwe6w%2FqqihOG%2FPA2jMEXpnEnBf1ItjoqKF7f%2F2B2wBgU20%2F%2FD3TeH3taTsf1hFBP8fFnCovTQ9cetFAEbJMma8rfrXB344fILQD79EwbrvLbvmEtDTkaM9Jna5ovW2txV%2BysOrovCp%2FHbmS76plA%2FDJ0iaLKIFHrF%2BwvdL3f3od3n0PfOIto3bKZiMaf4CjxXRq8FM0nObijBMhOXqRAYUaYBwp%2BvzGor%2BUVLU%2BAEfQstCEhqPcQPF5EtOU1gs5k%2BWzRMZulyARMjMhZWted2FJBVZkzxeYEuiI1v5KXrU9nO%2FUGWty3QUAdmoyo3TSZYEcppXDsV0k329C4daevumdd3G3VlsLpxuOR89JlFF%2FtOD9qYeNYGvmaoJ6isd9amHLOngygAeiVg%2Fn%2BV4iDcISMzOdDXig1Z5YEeuhDrEA3GWTA%2FQBquWKB8I4mbtgmUrg5O9XPUlHJFVZxEZ0BIUmpRIxblWWDgcrE5O6h51W5DcT%2B86G9gDxH8%2FN0QWlA1pp2hgoDcRjVSrhxiNpTDDrutvRBjqkAfp%2F6TONERyDefv61N2%2FXmAjEAga3ts0YS4H7%2FnOogCUCp7uIBw1FrdHKvUuGQECdDQEWpWUQ5aQB2O2v73LzONyhDurHqHo0cZpYnXUn5Jsed7X7ZvnCdYSeYOhF%2FYuuRiRHVdYAyqV73RV2z9%2F4%2BoZV4kg5dgaCB0yKmUEgYSifFzWelnKM0zwNnkPlFw7Tq%2BSrOz6YtTEjjs%2FJTeBxbp%2FX6U4&X-Amz-Signature=bd649a445d9aeb77b014739b462c6012e00f819ad3954d20c408b137860ea2dd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
