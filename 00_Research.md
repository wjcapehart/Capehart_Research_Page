# Research

## Making a Web Page on GitPages

Before starting you should first make a generic and blank web page 

Guidence for this is here.  ["Setting up a GitHub Pages site with Jekyll"](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll)

Once you get an empty project, you can then populate it.

It also may be helpful to push this tarball to your blank project.

## File Structure

The file structure that you should worry about is:

* /
  * _.config.yml_ (the configuration file - you will need to edit this)
  * __images/_ (a good place to put images)
     * *Department_Lockups_USE_THIS_ONE.png* (copy your prefered "South Dakota Mines 'M' Lockup to this name and it will auto-load when you push it to github.
     * *Department_Lockups_AES_CEE_white_trans.png* (AES/CEE Lockup)
     * *Department_Lockups_CEE_white_trans.png* (CEE Lockup)
  * __includes/_ (localized customizations for nominally compliant South Dakota Mines branding)
     * "If you change these files, it's your recipe and not mine."
  * _assets/css/fonts_ (local fonts sourced in the __includes/_ directories)
     * [Open Sans](https://fonts.google.com/specimen/Open+Sans)
     * [Spectral](https://fonts.google.com/specimen/Spectral?query=spectral)
     * [FontAwsome](https://fontawesome.com)
  * *LICENSE* (MIT License File)
  * _README.md_ (The Homepage and Introduction for your page.)
     * Any other "md" (markdown) files will arranged on the sidebar in numeric->alphabetical order.

## Editing the _.config.yml_ file.

For the _.config.yml_ make the following changes

```warning
Do NOT change the *remote_theme*!
```

| Variable                   | Description                               |
|:--------------------------:|:-----------------------------------------:|
| title                      | your webpage name as it will be displayed |
| email                      | your contact email                        |
| description                | a basic descrption of the page            |
| github_username            | your github username                      |
| sdmines_developer_homepage | your professional webpage                 |
| site.email                 | your contact email (again)                |
| url                        | your github repository for *this* page    |



## Markdown Files (*.md)

Content (i.e., webpages) are managed through Markdown Files with the (.md) suffix in the root directory of your web project.  

Markdown pages in your project root directory are visible on the sidebar and will be named by your first level "header" in the Markdown file. 

More tips and tricks are at [*01_Markdown_Tricks.md*](./01_Markdown_Tricks.md) file (Called "Markdown Tricks" on the side menu).






   




