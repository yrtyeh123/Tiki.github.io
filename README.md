
## Git và Github cho sysadmin

### Mục lục

[I. Mở đầu](#Modau)

[II. Ngôn ngữ Markdown](#ngonngumarkdown)
- [1. Thẻ tiêu đề](#thetieude)
- [2. Chèn link, chèn ảnh](#chenlinkchenanh)
- [3. Ký tự in đậm, in nghiêng](#kytuindaminnghieng)
- [4. Trích dẫn, bo chữ](#trichdanbochu)
- [5. Gạch đầu dòng](#gachdaudong)
- [6. Tạo bảng](#taobang)
- [Mẹo](#meo)
	
[III. Các thao tác với git và github](#cacthaotacvoigitvagithub)
- [0. Repo](#repo)
- [1. Cài đặt](#caidat)

  - [1.1. Linux](#linux)
  - [1.2. Windows](#windows)

- [2. Thao tác với Repo](#thaotacvoirepo)

  - [2.1. Trên Linux](#21trenlinux)
    - [2.1.1. Tạo mới](#211taomoi)
    - [2.1.2. Clone](#212clone)
    - [2.1.3. Add, commit, push](#213addcommitpush)
    - [2.1.4. Pull](#214pull)
  - [2.2. Trên Windows](#22trenwindows)
    - [2.2.1. Tạo một repo mới](#221taomotrepomoi)
    - [2.2.2. Clone](#222clone)
    - [2.2.3. Add, commit, push, pull ](#223)

- [3. Thao tác với tổ chức trong Github](#3)
- [4. Thao tác với nhánh (branch)](#4)
- [5. Issues](#5)
	
[Tổng kết](#Tongket)

===========================

<a name="Modau"></a>
## I. Mở đầu

`Git` là một phần mềm dùng để quản lý phiên bản của mã nguồn tương tự như `SVN` nhưng có nhiều ưu điểm hơn, `Git` đang được sủ dụng rộng rãi hiện nay.
Tuy nhiên trong bài viết này, tôi sẽ nói về git một cách "cá nhân" hơn, mang tính chia sẻ những cái tôi hay làm và hướng tới những người là sysadmin. Mong nhận được ý kiến đóng góp của các bạn.



