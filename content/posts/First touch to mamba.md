---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YQ4L55E5%2F20260913%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260913T235106Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJGMEQCIE3evuSI%2FuQqdl4jlLpoOd%2FGZ6y%2FEzbcXdY40ilH5Ae5AiA2abU9Qur7N8%2BRf%2Btpp%2FD64joMgKPVE0T0qQLJFUgAOCqIBAjZ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMpqJxASxXmg6Y5lYTKtwDN1T%2FuxGW4ZMZsGzh8Aelc4V7xmCS4JMVnuE8J55HnfTGCTsa5c1ay9BwJPskFrgdcS%2B59Z%2B0Bq88qDUnEPSJXQctaxO18yPtt7lAwPFECZR%2FjEkmFOYiOKctPFwm2yczcJ%2F04n9iJLrLDqE%2Fl5D%2BC0vw5%2FC%2F1Q2Tpuqgi1EUTbUnhZTSDCQbp2mecaOPMuPo0Glu%2FmCXZ%2BbQs7zSQL81%2FicBKtt%2BofcvRAWTOpBoMLdhDR1UdQCTodLHtZGzaxbjBbjZ01IsugsrRyWgsKXKHkYQd8GX7lrocBtkZualk4DC%2B090Q0mvjC%2FikQAuDrCV4vrVGzywPl07FJYfLRsv2G4lcL93fxcZEgmxaUypt1WAcsR%2B%2BT1bCKD1WnBUnbEyAu9QTuWizz%2Bv8ysB6VmtfOBj8T2XkKdtNDlc54GuFyWn5atZzzLkk%2BBzmUIyDZ0s9Tz4hVesXiqy6MLXj4txp1%2BROKgXhfsfQEhGnAGBOe2nti4pfzikiSR75X5MGipmsa8Gzc%2BS9CgwniW07ffCR1p1C1frNeS2TUSvHRSygrVFOj8wNME7aURDU6yAvqJOsOWmi%2FlZFlJZKhcVpCNAbq5wrdwb3LjioXk1CzlMicF5V54xpKrMw9ovgIYw%2F%2Bec1QY6pgF8HloV5Kj7x2x2AtSwiXs0TuukOxaB5%2F2wFDKOCjqlun%2BogCfWZDnFzGs8A9IRpKSufxprDqUWayIrwLjdia1hS9rBRetIKlmheJ9I75cSdEad5lesVf0hlE8Kopu6JtZDJpXYnCWNbHE4S0mfc9UUMYDBOKSk20U6czsjPPfaRF0lzQrK6VmT9mwjuSF2FLNT%2B73ncXae80IfcsVaKM5PUuWXGykv&X-Amz-Signature=d2cf846c69f2282358022ab3f451419e47875d953d0423d8069ee9a7e0f7e7a4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
