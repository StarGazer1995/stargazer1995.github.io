---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UFCGO3BU%2F20260812%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260812T222903Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA4aCXVzLXdlc3QtMiJIMEYCIQDl6VXhhs3u1CjjuoSei0z%2BWhhT4ZPv9RuWFwannssH4gIhAITpY0mFAuRmDM4xyrgncpOhyd6u5dHxkolPc%2FhRnmc3KogECNf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwkHQhoIrVFc6g%2BOgMq3AOSFiz3ODXizDZB4fiG8mvb4t1XnIlSGi9uNplywqykJMWG2aXvDIKgR4myYQ3YgonczeYc6GdwT18n0rDyPgG464XSIRZbEqRUlNsvhCV4Vhi1yNHoC8Pc%2Bop3qCXQmyMR44XSiBtEmc9if72B%2BWPHGIDB0ZLSurVhdYZv60ceoN4YvscMVh0XgUUTGwquJjTbCCSao9IOYddp6FVx%2BiogBWteiboDekZh9%2FByiB23Jy888c6BZYuvh4WOjDWiQHA3ZItp15Zsl4WF1uGp3dALfCYBQVqcIqALNJRMK4R5H8hnyF72xoyQnqXbNMMx7KJpVcFeCz1GX%2BiCd8PRUdkXK63d0L3I6Cxi4u6pSOpyxdDhbjmbTTPl2hjEfuFQ5n9VvbStP0OgUSVPNbGogyJoBVrgf4C3aFOGqIsYID52Rwarxooq0kwjwlu2Iz0fKZjvxce8400bpFOi4TM7VoELHnwtUlxbkq7Srj4KAErmGaDbf0EAzKfo2gufcbELlxXkWNaM%2Bb2et5Dnw8NbaB7el0xluD%2BwMihavlHppVgEXOVb5CK%2FoDs0qbxTn4gNMWlv1LGmh%2F45ThVnbr5OmC2nLSCpk6QPaDxcKGeAAzJvEELvzQbl2ZLoDDhymjCyzfPTBjqkAd4f4Aa3yNmsmCY%2F0dYqwus4JVtTLc75643SVRytPd%2BDtcSpt%2FejQysJbca1UG%2FlxghlpaLr8c1ryidD%2FoeYlJCGUFzFveI7VFpbbo7Ksy3iJB6mu5vILljxIHmDIUEBdEMWvSJdC%2F2OO5tmVL%2BYW7n3OrdF2WF57G4704PSVBlVkCqJdh457dDYjg9DrugD4e301s6T6EIru6DkCZiV3LJl2M5%2B&X-Amz-Signature=c72804f2f35695579444a43cf1320c807fb3041c32670aeea5b51d63b42326e2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
