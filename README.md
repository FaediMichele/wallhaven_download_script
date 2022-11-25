# Wallhaven download script
This script download a batch of image from the website [Wallhaven](https://wallhaven.cc/)

It create a file called "*wallhaven_config.json*" in the *Documents* folder of the current user.

The script read the file every *x* seconds and download a bunch of image randomly sorted from the website.
The configuration file can be manually edited to change the preferred search tag, batch size, ecc.

If the search include nsfw, is necessary to create a file called "*api.key*" that contains the Wallhaven key. (see [Wallhaven api webpage](https://wallhaven.cc/help/api))

Thanks to [SYNC3D](https://github.com/SYNC3D/wallhaven) for the idea.