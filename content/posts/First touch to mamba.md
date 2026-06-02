---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZGXY23SN%2F20260602%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260602T204739Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJHMEUCIQC6K7oWr6Gk4WUeppVJummr8UU9NacTSF4gXxdwdYD2OAIganrD3tv0lBkBWmcrOTMeA3LdGXNr0FcRQMx05dXZC%2B0q%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDDcSDVyQ4r0Z6WEnDCrcA4UyN0YXm8fpmhYvpnFxLmOziIzJ97t5GYlzLwIWOf2bWU5fuL9B%2B%2F1JvGp59RuU18gr8wmtaqjN%2FrNuzqz3U3rCq7Ax3a24jMuAJzfct0q45UaTh92J9Cg8OU6fHw9RtyUd1pYlcu2Kf31bhrtELuhSm1%2Bzlp%2BxAC%2BVygrfe04XAFOZm6gKHQS4EoDC%2BvPMlaejFTL%2FoJBbqv%2FJt6wBZe%2FpTGZ%2F6%2F9g8CXMe4jv%2FKmgQRAGV%2FcRlrwt8YsNTU%2BUUjY4YYsjx02ezoFvACAOE%2FxbK8SKUfH13%2BJhgtMfL%2BB3uqDhjCU6TtwUFesQ2Eci%2Bk9IkbahwMfFYIHyVhwCiE4KqiNY8wD4jX8hM0%2FuhbygFXlxd9VL3tu21DPdilk3Zy4Lj0abyY2XpN8IVMXAsJIB3eQHi7YIWVeTx1hQdehB9OMddiSPitW%2BUfOPQGYmJJA8523qheR6b6HmojtuFh4D7jxfWBC2QrlA7RAwhWKHicRyjqwV4AGYbTposvPLDA%2Br4X7JNpJFtySgvA%2FTdF9JJVtoAGp2A1%2Ffj6QIXTyjejQiRDkRiG1Map3Qsq8b0NT64dj%2FM3%2FipmBgh5xErxlI4WgqXBcV0cUHBU6UwOrQk0f7wxUYPecYb66OMKzL%2FNAGOqUBfvW0l5apOXzGpitZvkNOiQL6uNSVSpeUM%2BXC9LNPV0CjLFFGOzqar8muanTA3JwYKcZKUSFxfrfObS2QLGMZiOrgLbY%2FsDvqYU7yWPOKQpa0T5RsOLieWG6C2GlFNwm0k1SwrU5ykOEHlGY%2BvN0%2F%2FWucClTCi0RbzvaHEwhLZ2jeJbKm99cerfjw8mHfaVkijXBUpJ0bt%2BvdbEM84G0zbZQU55GT&X-Amz-Signature=450ffe4d438b70f469cbe73ad863c9dcbc6670543555b23c441416715d00013f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
