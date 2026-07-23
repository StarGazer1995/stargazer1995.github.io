---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T5IZJXMR%2F20260723%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260723T154739Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJIMEYCIQDW5ajIjRKZUGFeNHXhac%2BjVtMQW4VM6WkdUlmwaDRqxwIhALpsLPusZG5ERF%2BnJZG3%2B9GWBQRzKZKPw8CNZZTx089vKogECPD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxifyKiKxIBv0icWScq3AMz43KR0ePcp1WJJzPjDZGaYSmTrXoGmSrgjaokIhTuPFK6D5Q20unkJeMOc%2Flz6W8ueEkXbZQIJ%2BVrxmc4MdtgwEAUWrl1LdtQ%2BmoDkcdb81YUAA59w%2Fdkp040qZKP4RkczBLYr1s8KfITkyvIWpGHRV6LJBJgSKoziFqXzkDPebpKH3HUv4wLbKOhXb9N98uICPCreEYMZhn9BlRTCcX%2BwXa0tKqHnAmyT5aOHcUgz2rSHcGKmM9vtQht34TwyJigvEoegEzpnah9TUpewx2j7auGYjH3Ilmm5%2Fu7tFFoBy216N2ZM5pacaiCscYcNk5Z%2Fh7PNptvQjD2gVCXFNZB6qvIwMP%2FMrdcJDmtWWxFB54dtM%2BG7hLW48Kf3nq8etDPid0duOzgmvv41kAjb5%2FyfEywWTL6iBxCiTsqbd8IKzMS8prAn0%2FXps7M%2BIMP9j0HNwHRGe5GRwOg1%2F8JFM%2FdQgzOg%2FyYBNst4IxmgXmNh5MxCILiFApe5OrAJ8WYmf87H7ccj8ujW0SfYK0SlEtKTlSHGzB08miw8bTeSPWo04hJOp%2Fr9WLlkcs4jyp%2FgAMKSVdrVRNpqIodJdfLk631j2MpLM0790p4Li1jKXRyEmJOpLw0x1XLKwzH3zCS14jTBjqkAZru9bBLXA4MB8jHMR4l2eUG5YxzXXlkU3zrp%2FBr4W1pZfnav81TSOHv6iaStEfdOjfvJgSpCZogOwiJedWXyKsYQbQtTklV3doCfkbtBu6SGd6YnPi6byIdo0%2BjyH0cv9F2EAsEeCbCK93RjwjZje4eDi1mdfBq9FGnsYTlQW7BKvWI5gogBv4eUi1RGV4xRKsUL4W7x9y6YlWfIP9b3swhyb%2Fu&X-Amz-Signature=b86e8d427ad94d9bc95e1fc8b4e7422d30424437be6a051fa5d365e676529bcd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
