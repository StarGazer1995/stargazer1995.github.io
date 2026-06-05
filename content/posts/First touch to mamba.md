---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROE4WAET%2F20260605%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260605T142056Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDC0XFOpF2CAZt7swSfvOBDmoh5YDndI9E9KM5dWUsjzwIgR06MIS21xKiQikeh%2B%2B7FQEUG8VQDhsOnqb2ANIK0VPUq%2FwMIbhAAGgw2Mzc0MjMxODM4MDUiDEZFym1WZer%2B4QM1xSrcAx9%2BfUb2fV5lJbsxDW%2Fp3FxPO6lun116I%2B304X8%2BPNgYfyCYdKODUh%2BVbkcEgpQvB2C8rxq9ErO25JRxWMH9QfS2QGZeCtaVhcY5KkyMBoHaDRoUcrCgTYPbJ3OrmVGArEUOaekTRU2qTMUPrcR7SOhgl%2BZL6RbO0k6ATtO9iqTaRYl8%2FhsGj%2Fewm1NG4wWBHp5h9lLWOMdaLda3uBed6BNrY%2F5px%2BR0ftXKPdIBDNakmh8HoqFLI4xKiREp%2F1yjnDhQJ0X5MkaeJFYi09xWj37ixFdh3O8RxG%2BwjkPfgKeBT79TZA2hJVBtyITgViKiKNvZ6jliSfnxhFtjzP6pUqGBOEtEvesxK7tL3EqMrp6%2B3kWpGYxQ74AU%2FmL77EOM7LaWiXXHfz5LqhwMI2NEwXRkgjjG9VtPdMLAhDZNvuXRWWbWXRqAstUVmX5GmIrABOypTQNTCVRdjWexaHoryKTsSQQSdwmVwfmCy4Ii9XFoV8%2Bf%2FwON%2Ferg0QIYXG4S%2FM3eR18ge4HTEF6puQIFw6P6zj1z77zY0wSYtflW8OdihddxiwX0JBHKymccxwUfIQYJXTBi%2BoGF1mj3SNJ54V8S2z4TeUSyv%2FWGgGztBv%2FYqRn4vxzP1axz4aKUMLiTi9EGOqUBrfqeSE4f4vZYVRA6MP%2Bqb%2FgUi0fMwgWTbn2UoHYbC5hQu98gBRjnQzj5Vey1H7DlAldrjKgylwp8nTTTeaQ%2FXmu1QM02VY6VykZOW9ElqkccRhHVU%2FsAJoPyTV4OIzR%2Bq4o5d6W%2BX76kZeAehkH%2FZ5I6trKi7bn%2FVJPUg2sB2hj2znBWAyHust%2FLD4j4TB%2FE%2FrVBT6udFHy6S4QllOCboRkB5QjC&X-Amz-Signature=fd818489ace066a4dd92b3672390935d937aaf094e21c76f428b7eaafe7b1805&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
