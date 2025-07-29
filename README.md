# bmwccids-to-bytes
A simple BMW Check Control ID to bytes converter, especially for BMW's G chassis can bus.

### Where do i get the CCID list from?


I could recommend you to look at this [repo's](https://github.com/gizmo87898/G30_Kombi_Controller/blob/main/cc%20ids.txt) ccid.txt file. there is basically every ccid listed.

### Usage on BMW's G chassis can bus

For sending Messages, the CAN ID 5C0 is used

bytes as followed:
```
0x40, byte1, byte2, 0x29, 0xFF, 0xFF, 0xFF, 0xFF
        |      |      |
        |      |     Byte 0x29 is for showing the error on Cluster, Byte 0x28 is for not showing.
        |      | 
        |      |
        Check the output of the py program.
```
So if output of the py program is this, with CCID 446 being the Launch Control mssg:
```
CCID 446 is in Hex: 0x01BE
1st and 2nd byte: { 0xBE, 0x01 }
```
the can bytes should look like this:
```
0x40, 0xBE, 0x01, 0x29, 0xFF, 0xFF, 0xFF, 0xFF
```
![bmw_m3cs_lc](https://github.com/user-attachments/assets/28160772-0d65-4556-8dc9-e7e4cb74ece2)
credits to Simão Leal for his questionable m3cs cluster.

It was tested on Idrive6 and Idrive7 based clusters. Don't ask me anything about Idrive8 clusters, they seem to be much more complicated.

For F-Chassis BMWs it should definetely work with 5C0 with the same bytes.

If there are questions write me on discord, my name is rishik250809 or just write a issue here.

Shoutout goes to exycal for crying around for 3 days staright because he didn't get the launch control message working on his cluster 
He also gave me the motivation to do this shitty python code because he also kept crying around asking chatgpt without a pro subscription thus reaching his daily question limit.

also here are some photos from [Exycal](https://github.com/exycalll) and [Simão Leal](https://github.com/simaopleal) because they are retards.

<img width="480" height="800" alt="image" src="https://github.com/user-attachments/assets/76f6473a-91ab-4cb9-b163-53c8f0101dbd" />

<img width="480" height="800" alt="image" src="https://github.com/user-attachments/assets/14600327-a1cf-49f2-b5db-784f1894e758" />


![bmw_m3cs_hcd](https://github.com/user-attachments/assets/71740224-2fc3-4984-9bb1-79c94f29932e)
