---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U2SIPLAY%2F20260918%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260918T015315Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJHMEUCIArTdqqAmpUhmSuKOjfCyhXvJMqVq%2Fgo2PaIq9AC5f%2FQAiEAwvc%2FkbWirQemJmv39%2Bbac0TCu%2BO49iCrKHB3E8M9Booq%2FwMINhAAGgw2Mzc0MjMxODM4MDUiDOJi1qnp1ZFdUnq1yCrcA37rARxI3S6ePGBqoN37FOQG%2FlypxB4djWk8YF6BJapiWOv2UGJA0Da2WdL18bdMwKHSSQe2ma6sxtANx%2FraAGnPgUNXf6lq5r%2FvUtDUAkfBX6KHqg1enV08edx8FW7C2Wblep6OYxlFXa0VOibGBICb6hYht6rq8HOBC%2FsKQcwwWP%2Bp4wJ1kS%2FFaemq0XhYp80vFFeQLklCq96En80RgONLw4GbMvG%2BqizFvyns8PWFMwqnko69e2%2Br7Ehqw5Jz6UGCZKkWvzXVsdE3m4m5RUKdRec1AY%2F7Hq%2B1BpG13FrWuWNqQX6%2FKI0ZKWoXWPxhMdAChjwppLo03UD6qUQ5HY7Sw9LCVQh%2FXaLDCypK8pkG%2BvBM6fpnq4GwPzs5CwK%2Bl2PkYsJyrzBLTd%2F65NzGyJs8JNxhN6p56JLeOnxdzF%2BXTX8i5%2FBjHaJA4yFhdQLyrSKhslmzhVUORRrAtOGCOHpthn5SSHk4plgWgsXs6TWmxNWOeL5x%2BcH%2FJcGJHrDFurSE%2Boczmi0DDGHq21HArZ0cDamtjrAB6Flp7JZtFlU1SlgxIW2BLDrG3RL369s8RcuBxRQ1ifhkXCqFWgaZasypWj9%2F1GvMJaq2ypg4yB14EXDTkV5GQxcu6EccMJCysdUGOqUBBNFfYveai0zrsLqvPWr93lQQCniv5F9BwVcp63RO%2BtMKc77w6zD%2B0jEfzgRy2v9%2BgLwVrcpveFKX0QCs2nsT%2B1yUqnpCWmf6S7wayRv9Y6JbkYwWvYdsq6j6zIl2jD0Ze4ULa9HPIzBah60EyFDtJTu9vq9%2FQSauXopJcFnFjrdlJokyc%2BFAQndGTicnWsH8rvaLkgY%2FLqzWsK2p3xTrmTa70dlS&X-Amz-Signature=f6cdc9aaf3487968cc481b9c987d293eeece65e91c1d2ade3e69007995a53cfb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
