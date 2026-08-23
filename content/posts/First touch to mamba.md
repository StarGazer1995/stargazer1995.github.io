---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663VXF7ADY%2F20260823%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260823T220951Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJIMEYCIQCpnZjLaF0C7WEP2wyB03cvR40nV2Eby9NHsQeruf3mowIhAL%2FxESZkKqGrcud8rWAxuZhISui5E5%2FvOV%2F0N6fCe2bzKogECN3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyCTtzunGidfdCE5hAq3AMmF5MuboYUgOucebrnvX2npIs3aIvTNBoLmtEa%2FrhPDDXcMIuV5FA68X%2FIVzJ3D4Ol36dIBZ0oiXe%2FGKw9Mg%2BQ%2FoiF%2F%2B1xf%2BAzlTmFOqmTKmeMdgFPBsIWrZ%2BB96CJ1mBGnM%2BLxbp9lopvZtO5VbuPuve1G02boG77Tr81lglFmU7b2GzgqnvJwHuFrjumoBxlMR5pdzQ%2FvvyPLeyJKBaMd6lOnsttc59Lh1yZxAze5RiaPg1Dr0ErhHxetfmWxpLQwGLXezc2%2FMIKnIlHq6ISlCgjNBa5lUkkylZCQ5KUAxi4%2BHna3zU6iSBwkKj8zEII7cj%2BH4g8y2a8Wo1kd63hPT1FQtOgIzXLkchuapsDz9X%2FxS6iDavVHl1q0JROZLrliXpinbMEqIOCpHYfhKeLc6owTbPoDRWbzhA8OBnNbLY4L9mHEJADfaxmf8OhTs9hMSg2BRswCJygfp57qAzpkkCUTo8n8QhUJJ5qGn6VoCN4VFfpZJTCaay8BCQ03jBESpe%2BZ8Qt4biMWW%2FQP4BwqiHwRMOI3CF3YvpG%2BPbKfkrU3G9srwxI9cMrcE5M4g44cI7buuC41xdTjW2co5e54aWnJ1cvF%2BxfxSt%2BCD2btAZHYNw8vAmtNLk3GTDfma3UBjqkAXYMDryCwghIcg9D%2Fq6QB3MmEvEVQO8fuFseaHu14u7YX60Kw6yfWj7nE9XNX%2F1piwdV2BzAO6Nb6zbmkDbT9uHyqQ15KKesGWwbLzVcQsdj4RhJaWuUp1DtUAQO32a%2F5ZL48Q%2FKpeF29%2FDcNFW9PZ4RoKh34j5ubYiQ9p1VWu37vPcX2qfTGEmr%2FcFlVxmMxtTSL6%2BAHd4KYRBt%2Fi0UkDpfabNL&X-Amz-Signature=1b528909a57f8fb3447852ac7c5299cdfba9b51add7e555a90a1a949f6e1ba73&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
