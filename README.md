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
It was tested on Idrive6 and Idrive7 based clusters. Don't ask me anything about Idrive8 clusters, they seem to be much more complicated.

I forgot how it is on F chassis, I think it's also 5C0 with same bytes? 

If there are questions write me on discord, my name is rishik250809 or just write a issue here.
