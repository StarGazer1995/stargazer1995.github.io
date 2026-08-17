---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TIFI5XL6%2F20260817%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260817T102104Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJHMEUCIQC%2FYDEi1hLqbECIEtiZK8Bs40IfO09tQloOrLDU2EyVkgIgBji%2B7CZFWOHruUWU%2BZ0HS3yipPp7N5dkud%2BAz6RyM7oq%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDMVM9N93rH1SQZo5PircA83c1k3C0M%2FcDr%2FEsUq5igcEJV3ywmNwcFa6BjgZaoQssPHPXrRTqDAcMWp37QzhC68fci%2B%2FD%2BQR5aZfeUYzRcfeVVyUf8C5LTN8e6GOB%2BOmUNIB%2BWrWJBp4Wv6O0E0xobJn3zujXw%2FaZ536Vrva2NM1CrVkMrSsB77QM5wBrAljuEPvutEPX9lp7pC3lM2V%2F74UkxMLNzTCyJzhssr4k7IDciypB8LlfecEL6Z2Nq0gFhLgxr2bfm1AHVa%2BmPcZ9BVuRjHPrtM6ROnprWkiPvo%2BxGpJK8Hd5tW2XVmQ7i2kXWVRyURotx9uiWj4cncd5JV%2FUI5jPgVJctR4AafyFIAyq9iekn%2BfeJTpmAAdhuuLWH6Ch%2B%2FmZQ%2BN%2FCtQj07FXbLDvPK556Yy56YaL7C8%2FY%2FoNT3kEGQGPgBhZGaO4PARLLzYBP%2Bp5WRWVmM4cGyv2QOxTV2SlR%2B5t45tO3r0UekhYRtpJihHPjTk1lyDYZD8yqlzf4HGtltClq%2BxquUMrUekMS6or5V5hzYTT8xouM5lnMBa%2BuZWfelJcOi7E36E5XguWRgg%2BlbeLH8G5%2FmVM%2FFUsN%2FfH314NeOudDGzl6kTs8TxIUunbE637wNwY9NExJ8CKSwRR8hT5DvpMLO%2Fi9QGOqUBu3Ab2V0lR2m%2F2YZbAPO1N03tQw2xAtaKxpRpTgtRFtD1OoONHqKswMPxkudZJ9eGnDc1teNi5Qxfw7Dif67cjLSQ%2BdhLnbfH56mi7h5m9UF7eZ0PMe4zdVen8368Ke7xvYAiP%2FjuDq%2BSMh2fyDcdclrYaOeVswYFLHHCLStPaGox4nXUoa9hQS7B89VlAjlE%2FkuE5pd%2FRFKtA03hAFg0tWj1%2FFh6&X-Amz-Signature=a138bada152c2acf995025f8e2c6fe40de72eaf35a0e9f738d409c871fa22d5c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
