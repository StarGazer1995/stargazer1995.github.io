---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SOSHGT5V%2F20260627%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260627T055112Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDCaWsApj8JZK2zLCkfI2O45YJFsMyZzXJeBRc%2FuhgJUAiEA31Ld7EQSndqweC74S8ew3dRnZdDZSfQ7l1WaqGpjLeQq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDATJFVWvz8jLqtiNByrcA44hcqQRwNLabMzQTtDxMcsDAQGeoeDX59gFLMUBotgXR9Ay0d0R43BeVFTJ%2BJWyDUE8nGG3gSQJ0pePl3kw4VdsKG5Nrc21EXkmkZOjga03XmO96tNcF3%2BD5jPcDx2UafMFLoaHE%2F3TLQhWlJx6SQtSDxq7d8mUFVit7LQWwXCkt29Ax%2Bg3A8Gcajwmveu5SPmWAesSRw76y46y4u5SIzekWddJP%2FIIv7d8%2F1UKGWvJKi43%2B8c4l93W9mdBg%2By%2F2k4T45srVddSInj4b2Tlzqbf7%2FsEpoB2vAQR8YI47OW0sBv19451s6Ev9fZVIbOi%2FNAWO4PAz5b1FCmF39H%2B3zlH4kVOPt6EKBx2dcqb03CUeLNa4qWLwoefwvQRpmyMcV2EszD05FHKCA00OPcNg20lkF9WpgdL9dkitSrcSprzasvTPceYG81pQAg8zvDkAEzkSOVBbNF%2Fj3K7NnKGTdkmvIL%2Bm3Et25aXd9ZAmpuxHilDJRtwmyfeXJGFg8s27dlXoqykZN83sJwZWv48U5sbLNOc5ftjgmZMo5BrjTIlwETLrlLQJEEMcH9FNbP7C5xxN2rN3HR82PSChg8%2BLq%2FH%2FHtxckYivxR54ylQj%2F9PM9e21Ads4XOcv%2Fl%2FMPay%2FdEGOqUBDmpW94Y3Nvy1paVXx%2B20U2cPjeNd6REyk4jJ%2Fo0XaG3Q2C2M6FuwptYon0ZjZiq%2FsdXgfGzxmPvq%2B%2BqxHRCqm7pEOYbAZM2wHxV7fwrMsk7LPz3ZONa5pCRCTYaXYSgXmDlHKqFZrbv8MvOaZe0p3h2ENdML7FiWchMIqe4iuWA2TAtOC3jL0BllxkSiuwutrMots3K77ILbjbx4aZPysWjOFMXs&X-Amz-Signature=5466dbb00748d1cf1b9a060b356951a831645622c5a9570d667fd7af5471247e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
