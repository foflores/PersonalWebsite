---
slug: why-different-versions-of-dotnet
title: ".NET Versions Explained (Framework vs Core vs Standard)"
authors: [admin]
publishDate: 2023-05-14T00:00:00-04:00
image: /images/why-different-versions-of-dotnet-featured.webp
types: [Explainer]
categories: [Programming, Web]
tags: [Dotnet]
---

.NET is a developer platform created by Microsoft for building many different types of applications using common languages and libraries. It was initially developed in 2002 exclusively for Windows.

Around 2015 Microsoft began working on an open-source, cross-platform version of .NET that was a complete rewrite of the original. This rewrite was initially called .NET Core, however, since then Microsoft's development and naming strategy has shifted leading to the introduction of other versions of the platform such as .NET Framework and .NET Standard.

While the name changes were intended to clarify Microsoft's intent, they created confusion, especially among new developers who found it difficult to understand the differences between each version and when to use them. In this article, I'll explain what those differences are and which platform to choose depending on your needs.

{{< toc >}}

## .NET Framework

.NET Framework is the first version of .NET, released in 2002. It is a proprietary platform designed to build Windows desktop applications, web applications, and other services. It includes many libraries and APIs for various functionalities such as Windows Forms, Windows Presentation Foundation, ASP.NET, and more.

.NET Framework only works on Windows operating systems and requires the .NET Framework runtime to be installed on the target machine.

As new .NET framework versions were released, the platform became increasingly stable and continued to gain new features. However, Microsoft realized that times were changing.

Developers were moving away from monolithic applications and businesses were moving to the cloud. While .NET Framework had many features that made it ideal for businesses, it didn't have the lightweight, modular, and flexible properties that were ideal for modern, scalable, cloud-based architectures.

This eventually led to the creation of...

## .NET Core

.NET Core is a new version of .NET that is open-source and cross-platform, first released in 2016. It is designed to build modern, cloud-native applications that can run on Windows, Linux, and macOS. It includes a smaller set of libraries and APIs compared to .NET Framework, but it's faster and more modular.

It includes support for containerization, dependency injection, ARM, AOT compilation, and many new features designed to build modern apps. While some of these features have limited support as of today, support increases with each new release.

When Microsoft began working on .NET Core, .NET Framework was the primary version of the platform and what everyone referred to as .NET. This was mainly because .NET Core did not yet have the same level of features that businesses and developers came to expect from the platform. However, in late 2020, roughly a year after the release of .NET Core 3.1, Microsoft was ready to release the next major version and wanted to make it clear that the new platform was ready for mass adoption.

This is when Microsoft decided to retroactively rename the Windows-only .NET to .NET Framework, and the new .NET Core to .NET. Not only that, they wanted to make sure the version numbers between the two platforms didn't overlap.

This meant previous versions of .NET Core (3.1 and below), kept the "Core" name, while the new version they were releasing jumped to .NET 5.

Along with all the name changes, .NET 5 brought a standardized [release schedule](https://learn.microsoft.com/en-us/dotnet/core/releases-and-support#net-version-lifecycles). This allows developers to make more informed decisions about which version to use for their apps. Developers who prefer the latest features can choose the latest version and know they will receive at least 1 year of support on a short-term support version. Those who prefer stability can choose a long-term support version and be certain they will receive support for the next 3 years.

However, there is still one more version of .NET we need to talk about, and that's...

## .NET Standard

.NET Standard is a specification of a set of APIs that are available across multiple versions of the platform. This makes it possible to write libraries that work across older versions of .NET, including .NET Framework and .NET Core. The main goal of .NET Standard is to improve code sharing and reduce fragmentation across different .NET versions.

.NET Standard can help developers who manage projects written for .NET and .NET Framework by allowing them to write code that will work on both platforms.

.Net Standard, like .NET and .NET Framework, is versioned. Each version includes support for different APIs and .NET versions. As of writing this, there are 2 main versions of .NET Standard that developers should consider, 2.0 and 2.1.

.NET Standard 2.0 includes support for .NET Framework and should be targeted when writing code that needs to run on both .NET and .NET Framework. It Includes _almost_ every API available.

.NET Standard 2.1 drops support for .NET framework, but still includes support for .NET Core 3 and supports every API available in .NET. This version should be targeted when working to update .NET Core apps to a supported version since Microsoft has dropped support for .NET 5 and below as of writing.

Microsoft has stated that version 2.1 will be the last version of .NET Standard because with .NET 5 and on, .NET will be released as a [single code base](https://devblogs.microsoft.com/dotnet/the-future-of-net-standard/#net-5-as-the-combination-of-net-standard-net-core) with standard included.

## Conclusion

.NET Framework is the first version of .NET that works only on Windows. .NET Core, now referred to as .NET, is a newer, cross-platform version that's faster and more modular. .NET Standard is a set of APIs that define common functionality across all .NET versions, making it possible to write code that works across both .NET and .NET Framework.

Hopefully, this makes it a bit clearer when trying to understand what version of .NET should be used when. Now that Microsoft has consolidated .NET into one version and adopted a standard release schedule, going forward developers should have a much easier time understanding what version of the platform will suit their needs.
