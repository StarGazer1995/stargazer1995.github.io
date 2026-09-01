---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZRC7JPQP%2F20260901%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260901T172957Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF0mFb8B8%2BUQGv5Sh8d5miLmecihGm%2B4GSWyNyIEYmfGAiEAwjfmhi7EGRUp%2BLeo%2FmbfRSg9rZ%2BzlLm%2BDntNP9OVYvgqiAQIsf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM8zX3zD6t0MZBSX7SrcA9X5v6vOYhq8pUuJdIAfiYKK1l6CHpCEwWYX%2F29BT4TBCODwWeLsc33oUFYnR1%2BMRlMy8vwFyUgwn7v53PmI%2BUroUr4alhSVUFnFtqTsrQhtqitUWGkgodoFuAPMzDK7DXVMY0x%2Bfr3we5nlEQ5HHG0bKO6dF%2Bbh%2F8YevURt3L688o%2FV87ssvt1mQPzG9vLom5FGmp0lqn%2B9%2Ff4CwGI8HQkrh2S6KZkerJSStbjn5jNcZEepjO1UGYUQoxLQChgXES0Vug2Kx4elIfxARIlPG3AtSI2le3ZIVGVlrqDO%2B%2FhSZKTt2LWmk9Ol8skAol%2BNNcsG7QhP4oINZyx5tE3FdSw35DtKYscuA9clHbBQQuddCn0RMc08IyL23%2FOHqPk8S9yxyxWzQlvN%2B82x%2BJLoI70qt%2FfULw1GNYgAexNpwv%2B8uFyN%2F%2FvtzOgUwzE8eZBCMLlfomTCzjU1LnROk75Vjr8Xmrj3pDDThJvAr2ugvnRXto09ELXJNvn2qBwpP%2BdlJlKGfJD8qFQiI2TN%2B7bNYubsZ7qqdWakXyoBPSVnZWXbFWWMTPoKYseWAJyDE4X0HJ%2BnXhs5OakZYD%2BKnIf%2FzvTXsAGNa4D767Zn26u%2FQsZ%2BfibtEJHuSkViwk9mMPvf29QGOqUBKxCzH%2FqFQAsM%2BUGNcatJrTylvgTAE6UwKxPvyKwyvbxeHQgyJywn8Vq954mSYDDNLUZGSVsGv%2BmYTR8TVFIhFNA0uLnTZQpq%2BESbalWa9k%2FUMRLxtJkjN3dSku3RBVBOROBMVshr1r3Gpo29gKONoWMALWCVB1HU4QXIKx8ZNxsqd2lAdmkzGA8BgtUe7WKWAzdgVI%2B8X3MG7MdJuRg%2FdShCEfG3&X-Amz-Signature=a043cb0ab5a00d8d1c36341e8042815f4081802eb8cbcd21af6e4606d8fe5501&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
