---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663AGWZJYZ%2F20260530%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260530T015408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJGMEQCIECjBdRfPObqpjCsQahrOmFXd%2FQ%2F%2F5Zcw2r37I6rrh%2BHAiAB9KQYoyrcsPIkZw6DTj3PtQ3kjpKB7fR4YV7057v%2FyyqIBAjT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMGhZGQEnzG%2B612p%2BiKtwDPnJ8DULpVeZS9uvm%2BZyrCGlG3Jz%2F5TmAKNn4Nb6UIu8lL6uO0zJSMpZ4Au9IRAA3mG1mfMQhUFtQqy%2FzdHJGTAl5JTKO4%2B2LwpRTFFodqp7v%2BKYbSDrkPWC%2FG5ZLtiECiKTCoxvPbvSXlASH6b%2Fhv9vESIOhwz7xZ2kv0aTEo2%2Bgpbh1uIlrlHYxsfoW8Q6Xfrx0Slum%2F8dTF6TgiCN%2FTBeKj%2Bs9Don3BSHk2vzlv87xR9CIXRH73Eb%2BZtWPdooR86VEZXutEfwfe%2BUH%2BwwLdse8ZW%2BFMKaPBbyCKE6vLE0bU84P61m8yJrYMC2NWBi8ZhoTVl%2FkEyHXfwShgP0kEEEUZSXudgddtjr2fsacFiVk32e2Rq5upyi7%2BmeA07jp4uz3wzMGaxniG1S4R06WVf%2FqzdftN%2FKOhwk8KmpKpVXyleuMe68GpEavVxa1fC4VC9tRSOtmVGwHL9pjsiBXRT%2FGPA2ca3VDDLEOxInh%2FaQvO7%2FdLCm93m78w%2Bj1C%2B1a9uuEhqOXviX%2B7DGAFJVPCV3r09%2Fts7tdvB3QvEVuxk5qMVBwl2D3ssx0ZukHOKEzZK7qfnkbo2uac7lLtgnHutldnt9vMJGng9ZBCW9dLndrJfVI%2FgPebEDW8mUw3vvo0AY6pgE8YYcaOYit1J03dkILJK%2BDI3EikPMGirkcBefV7%2FFlxSVGTu0Y5%2BZdvBEa6zHTI80yqcDNQPqgJ5fiPzTX39sf2RKk9KJaluzueUaP2qRO8XaFKKUzdVSLhhl%2BGPHouX0KgI0oX%2F4iJluy%2BlMF9rOoTsRpEzUbfEj5kNNcfOhEGjs2zh8Su0Etef8vQsI8nJoQonqYvyZFb1fTeYV17YBdODZFMtd2&X-Amz-Signature=0f80b88e31b1b18e7c44374f9cad2f7f9bc9c559a76d9ecab9702dc52b37a167&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
