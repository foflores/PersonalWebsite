---
title: "My 1st post"
date: 2020-09-15T11:30:03+00:00
tags: ["first"]
author: "Favian Flores"
showToc: true
TocOpen: false
draft: false
hidemeta: false
comments: false
canonicalURL: "https://canonical.url/to/page"
disableHLJS: true # to disable highlightjs
disableShare: false
hideSummary: false
searchHidden: false
ShowReadingTime: true
ShowBreadCrumbs: true
ShowPostNavLinks: true
ShowWordCount: true
ShowRssButtonInSectionTermList: true
UseHugoToc: true
cover:
    image: "<image path/url>" # image path/url
    alt: "<alt text>" # alt text
    caption: "<text>" # display caption under cover
    relative: false # when using page bundles set this to true
    hidden: true # only hide on current single page

---

Docker is a tool to help developers create containers for their applications to run in. Containers are isolated environments similar to what virtual machines provide. However, unlike VMs, Docker containers are virtualized at the software level so they don't run a full operating system. This means containers generally use fewer resources than VMs and are able to start up much faster.

## What Does Docker Do?

Docker allows developers to quickly launch applications without affecting other parts of their system. Developers understand the difficulty of sharing code and making sure the necessary dependencies for their application are properly installed on every computer that needs to run it.

With Docker, you are able to write a `Dockerfile` which contains instructions for creating a Docker image. A Docker image contains all the necessary dependencies that an application requires to run. Using the `docker build` command, Docker creates an image that can be shared.

That image can then be uploaded to a registry such as [docker hub](https://hub.docker.com) so that it is easily accessible to anybody else who wants to run your application. Anybody with Docker installed can use the `docker run` command to automatically download, create a container, and run your application.

## Why Is Docker Useful?

There are several common challenges in software development that Docker containers alleviate. When new members join the team, setting them up with a development version of the app can be as simple as installing docker and running a single `docker run` command.

It's also much easier to move between the development and production environments. Docker is great for setting up CI/CD pipelines, automated testing, and overall shortening the time between when code is written to when it is deployed.

Several tools are built on top of Docker, such as Docker Compose and Kubernetes, which provide a way to deploy microservices that can scale out or in as needed. When using the cloud, scaling an app horizontally is usually the most cost-effective, and docker makes it that much easier to do so.

## Installing Docker

The first thing you need to do is to [install Docker](https://docs.docker.com/engine/install/). Docker is available on Mac, Windows, and a variety of Linux distributions.

To check if docker is installed and is running, open the terminal and run the following command:
```bash
sudo docker run hello-world
```

If docker is running correctly, you should see something like this:

![Text showing a successful docker installation](/images/what-is-docker-hello-world.webp)

## Creating A Website With Docker

In order to see the power of Docker firsthand, I'm going to create a static website using nginx as the web server and package it into a Docker image.

### Setting up a workspace

To set up our workspace we need to:
1. Create a folder and `cd` into it
2. Create an index.html file
3. Create a Dockerfile

The following commands do just that:

```bash
mkdir docker-nginx
cd docker-nginx
touch index.html
touch Dockerfile
```

### Creating the website

Now, we can create our website. I'm gonna keep it simple and just give it a title and some text saying "Hello World!". To do that we can run the following command:

```bash
vim index.html
```

press the letter `i` and then type in the HTML:

![The text to write into the index.html file](/images/what-is-docker-vim-html.webp)

Save the file by pressing `escape`, then `:wq`, and finally, `enter`

### Creating the Dockerfile

The last step we need to take is to tell docker that we want an image with nginx and our index.html file inside.

The docker registry already contains a working nginx image. So the only thing we need to do is add our index.html file and create a new image from that.

Following the same steps we took with the index.html, we can edit the Dockerfile with the following text:

![The text to write into the dockerfile](/images/what-is-docker-vim-dockerfile.webp)

### Building and running the image

Now that the Dockerfile is done, we have just 2 more commands to get the website up and running:
```bash
sudo docker build -t html-nginx:1 .
sudo docker run -p 8080:80 html-nginx:1
```

And that's it. The website should be available by going to `http://localhost:8080`.

![The hello world website rendered in a web browser](/images/what-is-docker-nginx-website.webp)

## Conclusion

Docker is a very helpful tool to package and run applications in an isolated, lightweight environment. It makes working with many developers or many different applications easier by alleviating some common challenges such as dealing with dependencies and different environments.

There are also other tools such as Docker Compose and Kubernetes which extend Docker's functionality to allow orchestrating scalable multi-container systems in the cloud.
