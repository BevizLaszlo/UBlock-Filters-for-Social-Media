<p align="center">
  <a href="https://github.com/BevizLaszlo/UBlock-Filters-for-Social-Media/releases">
    <img src="https://img.shields.io/github/v/release/BevizLaszlo/UBlock-Filters-for-Social-Media" alt="Latest Release">
  </a>
  <a href="https://github.com/BevizLaszlo/UBlock-Filters-for-Social-Media/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/BevizLaszlo/UBlock-Filters-for-Social-Media" alt="License">
  </a>
  <a href="https://github.com/BevizLaszlo/UBlock-Filters-for-Social-Media/stargazers">
    <img src="https://img.shields.io/github/stars/BevizLaszlo/UBlock-Filters-for-Social-Media?style=flat-square" alt="GitHub Stars">
  </a>
</p>

<h1 align="center">uBlock Origin Filters for Social Media</h1>

<p>
  The uBlock Origin filter list that hides all distractions on major social media platforms to make usage less addictive and more focused. This filter list removes elements like endless scrolling, video recommendations, pop-ups, and other addictive features. By eliminating these distractions, the list aims to help users regain control over their time and attention while using platforms like YouTube, Facebook, Reddit, and more.
</p>
<p>
This tool offers a simple yet effective way to boost productivity. It is fully customizable, allowing users to selectively block or hide various elements to suit their individual needs.
</p>
<br/>

<p align="center">
  <img src="https://github.com/user-attachments/assets/9d0c1915-1052-4e0e-8da8-7c7f422d6428" alt="Example of blocked feeds" width="700">
  <br/>
  <em>YouTube, Twitch, X, and Reddit homepages with distractions removed</em>
</p>


## Features
<table>
  <thead>
    <tr>
      <th>Platform</th>
      <th>Blocked Elements</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>YouTube</td>
      <td>
        <ul>
          <li>Home Feed</li>
          <li>YouTube Shorts (filter list from <a href="https://github.com/gijsdev/ublock-hide-yt-shorts">gijsdev/ublock-hide-yt-shorts</a>)</li>
          <li>Video recommendations next to the videos</li>
          <li>Video recommendations at the end of a video screen</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>Twitch</td>
      <td>
        <ul>
          <li>Home Feed</li>
          <li>Recommended channels</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>X</td>
      <td>
        <ul>
          <li>Home Timeline</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>Reddit</td>
      <td>
        <ul>
          <li>Home Feed</li>
          <li>Popular Feed</li>
          <li>All Feed</li>
          <li>Trending news in search bar</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>Facebook</td>
      <td>
        <ul>
          <li>Home Feed</li>
          <li>Marketplace and Videos Navigation Buttons</li>
          <li>Reels Section</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>LinkedIn</td>
      <td>
        <ul>
          <li>Feed sort toggle</li>
          <li>Home feed</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>



## Usage

### Install uBlock Origin extension in your browser

<ul>
  <li><a href="https://addons.mozilla.org/en-US/firefox/addon/ublock-origin/">Firefox (recommended)</a></li>
  <li><a href="https://microsoftedge.microsoft.com/addons/detail/ublock-origin/odfafepnkmbhccpbejgmiehpchacaeak">Microsoft Edge</a></li>
  <li><a href="https://addons.opera.com/en/extensions/details/ublock/">Opera</a></li>
</ul>

### Method 1: Subscribe via CDN (Auto-updates)
<ol>
  <li>Open uBlock Origin Dashboard</li>
  <li>Navigate to 'Filter lists' section</li>
  <li>Scroll down to 'Custom' section</li>
  <li>Click the 'Import...' dropdown menu</li>
  <li>Paste one or more of the following URLs based on your preferences:</li>
  <br>
  <table>
    <tr>
      <td>All filters:</td>
<td>
  
```
https://cdn.jsdelivr.net/gh/BevizLaszlo/UBlock-Filters-for-Social-Media@latest/filterlist.txt
```
</td>
    </tr>
    <tr>
      <td>Facebook:</td>
<td>
  
```
https://cdn.jsdelivr.net/gh/BevizLaszlo/UBlock-Filters-for-Social-Media@latest/facebook.txt
```
</td>
    </tr>
        <tr>
      <td>LinkedIn:</td>
<td>
  
```
https://cdn.jsdelivr.net/gh/BevizLaszlo/UBlock-Filters-for-Social-Media@latest/linkedin.txt
```
</td>
    </tr>
        <tr>
      <td>Reddit:</td>
<td>
  
```
https://cdn.jsdelivr.net/gh/BevizLaszlo/UBlock-Filters-for-Social-Media@latest/reddit.txt
```
</td>
    </tr>
        <tr>
      <td>Twitch:</td>
<td>
  
```
https://cdn.jsdelivr.net/gh/BevizLaszlo/UBlock-Filters-for-Social-Media@latest/twitch.txt
```
</td>
    </tr>
        <tr>
      <td>YouTube:</td>
<td>
  
```
https://cdn.jsdelivr.net/gh/BevizLaszlo/UBlock-Filters-for-Social-Media@latest/youtube.txt
```
</td>
    </tr>
    <tr>
      <td>X:</td>
<td>
  
```
https://cdn.jsdelivr.net/gh/BevizLaszlo/UBlock-Filters-for-Social-Media@latest/x.txt
```
</td>
    </tr>
  </table>

  <li>Click 'Apply changes'</li>
</ol>

> [!NOTE]
Keep in mind that auto-updates take some time to update

### Method 2: Download from Release
<ol>
  <li>Download the filterlist.txt file from the latest release <a href='https://github.com/BevizLaszlo/UBlock-Filters-for-Social-Media/releases/latest'>here</a></li>
  <li>Open uBlock Origin Dashboard</li>
  <li>Navigate to 'My filters' section</li>
  <li>
    Click 'Import and append...' and select the downloaded filterlist.txt file <br/>
    Alternatively, you can simply copy the text from filterlist.txt and paste it into the filter input field.
  </li>
</ol>
<br/>

> [!NOTE]
><ul>
>  <li>Although this filter is designed to improve focus, it may alter the user interface and functionality of some platforms.</li>
>  <li>Be aware that platforms may make changes that can break the functionality of the filter, so it's important to stay updated.</li>
></ul>
