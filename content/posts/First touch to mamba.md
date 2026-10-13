---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VTFYGUHP%2F20261013%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261013T014334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDT6ZrTf9W5UXHqyCCzSzUcSzZTQ9K6hlN9ldAZFHQCyAIgBIKexvv45wFn3IFY%2FvBbP1X5ud%2B2kJdQ0UScL0Tvfv4qiAQIkf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGjt5lPZf0Ibc6ZW9CrcA%2BiDM6htQX0f0H2dJJ1kzgvRm7CwvcM4fX1HdiTmuNkJlLQBNMF39m6LOQCD7lKCKgsQ6Z%2BhlIsLGa4qHRr1lDHUEuMvcIRtETxa8Fhvnyoif1kD1lGBuj4404wCtuPRBqErxmNKwDsizF3l4MCItzGvyg3qxzLGKooaGF9Bwel63fVs0D0UTrxs6zyrfVNBm%2FtjbdW8BJeb3Gpx2Cilj5xR1A99GhhaeSk7bbLnm%2F6ZKsduptZNbj6%2FLVBlq%2F4AWIPU2FDFA7vPA1AVrZ5k8i3OCq2Us%2FfA88ZAtArQU3Cyu9DWzfnEGLgIp5AlYqjZvuy7Bb6piJmf1BUhAUsPRDrDdYeiNB6HMXJO72vFdymDEUD5Oa8zOSNplvMXXIcbTFx%2F6ys5BTzdIqNIJLnUKBus2OCGq1tHj4CFRI%2BsSJU%2BtLMNO%2FkEIC5XW1ujXPr4iRVerte%2BnXptsJB3kCAc%2Bx7XYdFqHck%2BB5M3XFldAT4WQoeOmcIYmF9eIUAOnp6JivIso3WdI5c1E9uEWd2Zb5F4EDtnkX0E6UrrM1QG3YbIBC8faXKFM69e1XVLdOg0Oec%2FI2DdEFv0R30mT5AXCrLAYUvzKr8jgkiRY9VCNbZ5uFM5KGP7FCGx0mNfMPvltdYGOqUBq3XRQpgmMdF8Kg%2F5MWUOd8o%2BnveT3JhdHEnm7JLAkcIxMLcX86ETUeWJW9bqOW0X%2F4Ef88FCZcoG1nx2mDQj3%2FnDW3czjhdexD%2F%2F7fuSrSRUvvuZdigCoSgtfgvinch%2BIkAeNgCfpVVquLkxJzJvCTTgYTJ3yyJvQid7g8FjVOIKGx09QBldEwMUAWMv4onOBWLf9oGmJe%2B8iAvmd7xlKbcMkL6B&X-Amz-Signature=54cfc2644f19d9c5299fd6e1d93a746bf3645d5832787635ff586e3120f9d05c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
