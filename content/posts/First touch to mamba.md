---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YUF65EO4%2F20261005%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261005T001830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJIMEYCIQCx9R38lk38Qv%2BSrXIs0O%2FhiGkOCRUQoQXhbljZp76mBwIhANqGUfUnQ4KKDlIHPF%2BdG6TyBaYOEtt2x4Dd%2FOW9i7S1KogECM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwqZ7wkOmQwywiSc8sq3APPw4a6%2BU24Rw5C6cWfifeFrb53JLxAgjDi9ylWRRpCPZoMcfSeyiWrV%2Ff5GkwUYwGsmHdkUzdxi8DfySvV2dUm%2BXmHZQ604YhgbiS3K5qDpIw2Vd8VUQym1hivc1P148LeZQtm2a9Qlv8MKk4HqnmyC1HzHQrPkQH5hO%2BEPrpTMxmcMLIrhLLf9HXkqcZl1fdCaIwghDgDz3VVEB%2BXk6rTaG%2Fgpg11xh5e8ZPDaI7DKwCqlaRC3rerDyqJoYvsClYwSLDyCgrJCd%2F7kes5yHSs8N3ZARXO3VmSanznxOTMwZRmzhZUaJL5aMnJG24eLv8ngihYtjkM%2Fu04kEslAAOq1MTcQRyhsZHGYAzidLMC229pQquFYwcpWg8YNn5eUGgplQ1iaZLyl8pCmpEr5g62jql5e1AQOwQGSfD54KFEzT%2BU2WRiGNtNGHo%2BwzpvxZuD1i7FKOPlZoR9dkO%2Fw7z%2Fqte52sQuOzlBksOpLSXxKdmVj3nEg37qy%2FwFawMxfZkZTZZKpIvoS00NSl1vyrq0qouhtlpbwzz1cvd8KWVVooXf3HGO8Xafrt5ohuhISR6ZVx3G7tCumZHZ7lRCFDtXrmAB5mnyN449QW1kif93cs5Q%2Fspu0y33uLCCWTCznYvWBjqkAc2DfI3wuyTUCh4oPX9EaWU%2Blr7o26Rcr05vaoQPp%2B07y4z3PvRGScJxX%2BBDkSs4DY9UdC%2FecUq2yVCyiCz%2BA34Zk%2BWXMSRNZi8jiPZ199MqCmbhn81Vc3JtakbbcH6XotbHgXdMn7AcUUawkBcPaSXypzi02vq6NBmfvxdfXVIe8TcEgTdbx6CzGVMa6tiBVuiqhoUhgRGLBRYPPeLyNQndgmYG&X-Amz-Signature=bd5f1344dbd94201932cc5b1014a924b426c0b9c5c8226884964cd1d7a791f65&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
