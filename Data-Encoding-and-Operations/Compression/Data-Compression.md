# `Data Compression`
---
`Covered in this file:`

1. Data Compression Defined
2. Lossless Compression
3. Lossy Compression

# `Data Compression Defined`
`Data compression` is the process of reducing the size of a data file or stream without significant loss of information. 
> * The primary goal is to decrease the amount of storage space required or to increase the speed at which data can be transmitted over a network.

There are two main categories of file compression:
* Lossless Compression
* Lossy Compression


<br>

---
# `Lossless Compression`
`Lossless compression` is a type of data compression technique in which the original data can be perfectly reconstructed from the compressed data without any loss of information. 
> * This method reduces the size of data files by identifying and eliminating statistical redundancy. In other words, it finds patterns and repetitions in the data that can be represented more efficiently.
> * Lossless compression is typically used for text files, software, and certain types of images (like PNG and GIF) where preserving the exact original data is crucial.

<br>

Lossless Compression:
* No loss of Data
* Reversible Process
* Typically used for text files, software, images.

<br>

Examples of Lossless Compression Algorithms:
| Algorithm                     | Description                                                                                   |
|-------------------------------|-----------------------------------------------------------------------------------------------|
| **Huffman Coding**             | Uses variable-length codes for frequent symbols and longer codes for less frequent symbols.   |
| **LZ77 (Lempel-Ziv 1977)**     | Finds duplicate strings within a sliding window and replaces subsequent occurrences.          |
| **LZ78 (Lempel-Ziv 1978)**     | Builds a dictionary of sequences and replaces subsequent occurrences with dictionary references. |
| **LZW (Lempel-Ziv-Welch)**     | An extension of LZ78, dynamically builds a dictionary, used in formats like GIF and TIFF.     |
| **DEFLATE**                    | Combines LZ77 and Huffman coding, used in formats like ZIP, GZIP, and PNG.                    |
| **Burrows-Wheeler Transform**  | Rearranges data to group similar characters together, aiding further compression.             |
| **Run-Length Encoding (RLE)**  | Replaces sequences of repeated characters with a single character and a count.               |
| **Prediction by Partial Matching (PPM)** | Uses statistical predictions based on previous symbols, compressed with arithmetic coding. |
| **LZMA (Lempel-Ziv-Markov chain algorithm)** | A dictionary-based approach with high compression ratios, used in the 7z format. |
| **Range Coding**               | Similar to arithmetic coding, encodes data into a single number using symbol probabilities.   |


<br>

Lossless compression is often used alongside file archiving.
* Formats like ZIP and GZIP use lossless compression to reduce file sizes while allowing for exact data recovery.

Some Image and Audio Formats also use Lossless compression.
* PNG and FLAC are examples of lossless image and audio formats, respectively, where no quality is sacrificed.

| File Format | Extension | Description | Common Use |
|:-:|:-:|:-:|:-:|
| ZIP | .zip| A widely used file format that supports lossless data compression. | File archiving and data compression. |
| GZIP| .gz | A file format and software application for file compression and decompression. | Compressing single files, often used with tar for multiple files. |
| 7z| .7z | A compressed archive file format with a high-compression ratio algorithm (LZMA). | General-purpose file compression with high compression ratios. |
| RAR | .rar| A proprietary archive format supporting data compression, error recovery, and file spanning. | File archiving with additional features like error recovery. |
| TAR | .tar| A format used for archiving files without compression; often combined with GZIP or BZIP2. | Archiving multiple files into a single archive before compressing. |
| FLAC| .flac | An audio format that compresses audio without any loss in quality. | Compressing audio files while preserving original sound quality. |
| BZIP2 | .bz2| A compression program using the Burrows-Wheeler algorithm. | Compressing files in UNIX/Linux environments, often used with TAR. |
| LZMA| .lzma | An algorithm providing high compression ratios, used in formats like 7z. | High-ratio data compression. |
| XZ| .xz | A file format using the LZMA2 compression algorithm. | Compressing files in UNIX/Linux environments with high compression ratios. |
| ALAC| .m4a| A lossless audio codec developed by Apple. | Compressing audio files on Apple devices without loss of quality. |
| PNG | .png| An image format using lossless compression, ideal for images needing exact precision. | Storing images with transparency, text, or requiring exact reproduction. |
| GIF | .gif| An image format with lossless compression, limited to 256 colors and supporting animation. | Simple images with limited color palettes and animations. |



<br>

---
# `Lossy Compression`
`Lossy compression` is a type of data compression technique where some amount of data is lost during the compression process. 
> * The goal is to reduce the file size significantly by removing certain parts of the data that are considered less important or that the human senses can perceive as redundant. 
> * Unlike lossless compression, the original data cannot be perfectly reconstructed after decompression.
> * Lossy compression is widely used in multimedia applications where a small amount of data loss is acceptable to achieve significant reductions in file size, making it easier to store, transmit, and stream media.

Lossy Compression:
* Loss of some Data
* Irreversible Process
* Smaller file sizes than Lossless

Examples of Lossy Compression Algorithms:
| Algorithm                     | Description                                                                                   |
|-------------------------------|-----------------------------------------------------------------------------------------------|
| **Discrete Cosine Transform (DCT)** | Used in JPEG and MPEG, transforms spatial domain data into frequency domain, enabling compression by discarding less important frequencies. |
| **Quantization**              | Applied in various formats, it reduces precision of data, which helps to compress but also loses some information. |
| **Transform Coding**          | General approach used in algorithms like DCT and wavelet, converts data into a different domain to facilitate compression. |
| **Prediction**                | Used in video compression (e.g., MPEG, H.264) to predict frames based on previous ones, reducing redundancy. |
| **Motion Compensation**       | In video compression, it estimates and compensates for motion between frames to reduce the amount of data needed. |
| **Wavelet Transform**         | Used in formats like JPEG 2000, transforms data into wavelets to efficiently encode both high and low frequency information. |
| **Subsampling**               | Used in image compression, reduces color information to compress data, often applied in JPEG with chroma subsampling. |
| **Perceptual Coding**         | Used in audio codecs like MP3 and AAC, exploits the limitations of human perception to remove inaudible parts of the audio. |
| **Transform Coding (e.g., DCT, FFT)** | Converts data into a domain (e.g., frequency) where compression is more efficient. |
| **Lossy Run-Length Encoding** | A variation of RLE where only a subset of repeated values is encoded, used in some image compression schemes. |

<br>

Lossy compression is often used for images audio and video.
> * JPEG is a widely used lossy image format, where the compression reduces file size at the cost of some image quality, often imperceptible to the naked eye.
> * MP3 is a common audio format that reduces file size by discarding inaudible frequencies, making it ideal for music streaming.
> * Formats like MPEG-4 use lossy compression to make large video files more manageable without significantly compromising visual quality.

The trade-off for Lossy compression is Quality vs. Size. Higher compression rates lead to smaller files but more noticeable loss in quality.

Lossy compression is highly efficient in reducing file sizes, making it suitable for applications where storage space or bandwidth is limited.

| File Format | Extension | Description | Common Use |
|-------------|-----------|-------------|------------|
| JPEG        | .jpg, .jpeg | A widely used image format that compresses images by discarding some data. | Photographs and web images where reduced file size is prioritized over perfect quality. |
| MP3         | .mp3      | A popular audio format that compresses sound by removing frequencies less audible to the human ear. | Music streaming, portable audio players, and online music distribution. |
| AAC         | .aac      | Advanced Audio Coding, designed to be the successor of MP3 with better sound quality at similar bit rates. | Streaming audio, Apple devices, and digital radio broadcasting. |
| OGG Vorbis  | .ogg      | A free, open-source audio format offering high-quality compression. | Streaming and storing music, especially in open-source applications. |
| WMA         | .wma      | Windows Media Audio, developed by Microsoft, offers efficient compression with decent quality. | Streaming and downloading music, especially in Windows-based platforms. |
| MPEG-4      | .mp4      | A multimedia container format that compresses video, audio, and subtitles. | Video streaming, online video sharing, and digital downloads. |
| AVI (with MPEG-4) | .avi | An older multimedia container format that can use lossy compression for video and audio. | Video playback and editing, particularly on older systems. |
| WMV         | .wmv      | Windows Media Video, a video format developed by Microsoft that uses lossy compression. | Streaming and downloading videos, especially on Windows platforms. |
| WebP        | .webp     | An image format developed by Google that provides superior lossless and lossy compression for images. | Web images where both quality and reduced file size are important. |
| HEVC (H.265) | .hevc, .h265 | High-Efficiency Video Coding, a video compression standard offering better compression than H.264. | 4K video streaming, Blu-ray discs, and high-definition video recording. |
| HEIF/HEIC   | .heif, .heic | High-Efficiency Image Format, often used with HEVC for images and sequences. | Storing images on Apple devices and high-quality image sharing. |
| DTS         | .dts      | A multichannel audio format used in film and home theater, offering high-quality compression. | Surround sound in DVDs, Blu-rays, and home theater systems. |
| Opus        | .opus     | A versatile audio codec with variable bitrate, optimized for both low and high bitrates. | Voice over IP (VoIP), streaming audio, and live broadcasting. |
| AMR         | .amr      | Adaptive Multi-Rate, an audio format optimized for speech coding. | Voice recordings, especially in mobile phones. |
| RealAudio   | .ra, .rm   | An older audio format that compresses sound for streaming over the internet. | Streaming audio, especially in early internet radio and web audio. |
| RealVideo   | .rv, .rm   | A video compression format developed by RealNetworks for streaming. | Internet video streaming, especially in the early days of web video. |
| VQF         | .vqf      | A less common audio format that offers better quality than MP3 at the same bitrates. | Audio compression, primarily in Japan, though it is now largely obsolete. |
| DV          | .dv       | A lossy video format used for digital video recording. | Digital camcorders and professional video editing. |
| Xvid        | .xvid     | An open-source video codec that uses lossy compression, based on MPEG-4. | Compressing and sharing video files, particularly in peer-to-peer networks. |
| DivX        | .divx     | A video codec that offers high compression while maintaining relatively good video quality. | Compressing and distributing video, particularly over the internet. |

