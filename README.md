# Subtitle Warp
Corrects not only offsets in subtitles but also the speed according to first and last lines

`python3 subtitle_warp start end filename`

where there are:

`start`:    Spperance of the first subtitle line format: 00:00:00,000

`end`:      Spperance of the last subtitle line format: 00:00:00,000

`filename`: Name of the srt file. It will be replaced!!!
            Except the file has the format: [name]-pre.srt then the new file will be [name].srt
