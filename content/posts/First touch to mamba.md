---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SI7A7LVP%2F20260807%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260807T222426Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAvEeEMFQhSKhPk%2BidydqmLtheQnLfcz2MFqZwZoOp8%2FAiBoR5CgxTp5ZqrjYkQxJasTR5leDHv6uPvKCj7eHzD3XCr%2FAwhfEAAaDDYzNzQyMzE4MzgwNSIMbeQOyOOsry1eDqBTKtwDQkgEHiGJ%2B7yMAzJFCBUXkeL5WSUWCq%2BeqCzJBemmEE4eFmAQQ%2FXJael3snWrdgUdECJ%2BCwFyoSMjZknvuM9rY3KyKoyvctzuHcqkd9Te6aCTSeDDxQVIz5RWR2sofGJ2tg%2FbO7pOD1iD6jzQjg4W4URTL642R%2BBf%2F%2BuklLItImRoD6jdkgmdhRN1KVWZywpBtYW%2F0icLBIEbit5bhcL8cbOWLvYUmbgs21ToV1j0WMWoWQn%2FmMaLP4fpPdHyUKEG%2FvoaCwpQ2Mgxqai0zDueISFyYT41eAbXOdxdlXXsMuhKtMS2Nv7Da1V9CQJycDVrfUReMAxIEHoM10SOTk%2B%2F6TFp0kb5kp8lbwyu0XzkHzvvpVkxrY7mOGDtWwQnd0%2FVStD8XISfObOSQOZUe2VLM9jZKXIStalO34CiCKNX4Ni8SybtD1O3iOb9aD1D7GDFTnlqd9WDiJLcVr%2BDj797syZdQX6FLVtqpGJS561sKAuDHTzQwEJ%2FKtqDIEHOv8R1vlGTTZk2FQniTxlMRDRAUHbkW1EemuqJEIVApkI3voDKmCn41yPkMNdok4yq3rp%2FjLGIfTUdeDgooBTsKEYUriZHPzlFZqnA2Q2qgwGv2WWDkiPX2AuMo%2Btv2Jkw0rTZ0wY6pgEj34UuJyD8awa11Zb5%2FA0iWhEAijNTdPJGmVSXfcMFlza7l4GrYAN27IzVSjOFFJBafnv%2BOLgBvHzEoDoERRZYuZHQJF%2FtyTYtd7xMVbrkbzOL8axeith58luGXzboqKWVoSUEHDO%2FvVCQEr%2BRRTI%2Fvi5T4agmyNtDhQLMaj94wtT%2FwTjn5kd3BBfF04Rj1a17ZMD6lHeeFCoyA3VzQ%2FQqUnt4Yfkr&X-Amz-Signature=30f4f9097e3be5e4eb606baaa13f66be4a8c725003e7867d3cf627aa2c8fdb8a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
