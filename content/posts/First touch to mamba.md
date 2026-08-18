---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UMXIQZJB%2F20260818%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260818T003623Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDeYR%2BLACUgGcpnKGr9gkoGrU%2BwgrkvBeMNKrBsjbzcogIhAJ768rQgLNUqqAAyE%2Fhjc1zl5ilVifa4V4sVhkuT6lyfKv8DCFAQABoMNjM3NDIzMTgzODA1IgyBtBAXjNk4iyuBagMq3APWnvwezjnxHaI01Tq1Rx8NgyWpp39tGI%2BGod7DUwhBUByPquMYnmK7Hc%2FHdiCdL942EqkaHu%2BGm5EyOgh12D3C2FZsnhEmNhWapHMpiD0qIKy61Rk0kpyGL0cJ1yeARowbQf5obv%2ByucyXzfCpgkQzC3pDhjog3s2txPBe2ymz40dsktg0w9jhPKPHbn%2BVbek3kWmbWLPWYcd2F3HCs6meBa51aSEcf7xlbTKducEjoIpGOwLDqHIvQMWxrIqmtxjNLU%2Fll3xF5493Hff4pVTe1KYRAgSbsc0rvBCNC%2FpgeRZmPXBrpnsR7dDZpjvKI%2FCwxPWW%2FA3tT55MtORxm%2BOUEMn4o%2F9RCEqAooF4jo8YkMi7Jtq6YMPtp1Nnte1yMskFNm0BxvDfXIelPTBtU2Q7cKOsJQWgtojx38KJHqt4QciYb1OIzUJ5BDb%2F%2FaTLktVKwe1tzX%2BnpW7LUmVuyJrAR0mzOPImReXzBTiiDl5YJt5UCZbheuYZldUojst4QuQuSj9k7AuX%2BiVDDg3EyVHvVmKfU9ehfpVQwfXcSBWPGUuxMz3OCoqv1VTOsI79XwKiVk2Jjf9kLYyNL0fAx%2BYgdsc450CrFuhinJMixzea4vEulte0GyVpqdFUJzCenI7UBjqkAeoimGv0w5YhSrNRsEEI0NuYbXs%2FclOIM6Hp5YB4DGW4iS356Iw%2BmMN1sYkSnTdsOtCfHRQXbvfwiDdREfCHrWxIA6Cdy52qa5lamZTmKM4rpdHFhg%2FrLxPkzp%2Bl3jsPHjxFHbVFZ0qM9KKKebMf6%2FY5s2h2zIPrVnjeyuFiesCCQKzC7FvnZMb7hdf5ta%2B7TIeWhZADCNLC0dHNgRJRg53OI9ei&X-Amz-Signature=e761f52ef1c56555b869a3c2538ce8217702f9c5d3ee4eb31521fbad5279c351&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
