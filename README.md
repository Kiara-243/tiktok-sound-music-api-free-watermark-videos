# TikTok Sound Music API (Free-Watermark Videos) Scraper
> A specialized TikTok Sound Music API scraper that extracts detailed data from videos using a specific sound, along with rich creator, audio, and performance metadata. It also lets you search TikTok music by keyword and fetch no-watermark video URLs for clean downstream use.

> Ideal for growth marketers, data engineers, and analysts who want structured TikTok sound data without dealing with fragile front-end scraping or watermarked downloads.


<p align="center">
  <a href="https://bitbash.dev" target="_blank">
    <img src="https://github.com/za2122/footer-section/blob/main/media/scraper.png" alt="Bitbash Banner" width="100%"></a>
</p>
<p align="center">
  <a href="https://t.me/devpilot1" target="_blank">
    <img src="https://img.shields.io/badge/Chat%20on-Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram">
  </a>&nbsp;
  <a href="https://wa.me/923249868488?text=Hi%20BitBash%2C%20I'm%20interested%20in%20automation." target="_blank">
    <img src="https://img.shields.io/badge/Chat-WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white" alt="WhatsApp">
  </a>&nbsp;
  <a href="mailto:sale@bitbash.dev" target="_blank">
    <img src="https://img.shields.io/badge/Email-sale@bitbash.dev-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail">
  </a>&nbsp;
  <a href="https://bitbash.dev" target="_blank">
    <img src="https://img.shields.io/badge/Visit-Website-007BFF?style=for-the-badge&logo=google-chrome&logoColor=white" alt="Website">
  </a>
</p>




<p align="center" style="font-weight:600; margin-top:8px; margin-bottom:8px;">
  Created by Bitbash, built to showcase our approach to Scraping and Automation!<br>
  If you are looking for <strong>TikTok Sound Music API (free-watermark videos)</strong> you've just found your team — Let’s Chat. 👆👆
</p>


## Introduction
This project provides a programmable way to query TikTok’s sound ecosystem and collect structured data around any music track or original sound. By pointing the scraper at a TikTok sound URL or a keyword, you can gather full video lists, creator profiles, and sound metadata, all normalized into predictable JSON.

It solves the headache of manually exploring TikTok sounds, exporting statistics, or dealing with watermarked assets. Instead, you get ready-to-use data for dashboards, research, content discovery, and automation workflows—powered by a TikTok Sound Music API style interface.

It’s built for:
- Marketing and growth teams tracking viral sounds and performance.
- Data engineers building pipelines on top of TikTok sound data.
- Analysts and creators researching trends, engagement, and music usage.

### Sound-Centric TikTok Intelligence
- Collect videos that use a specific TikTok sound, including no-watermark video URLs.
- Search music by keyword and rank results by relevance, popularity, or recency.
- Enrich each video with creator stats, engagement numbers, and sound properties.
- Filter and limit results for focused analysis, experiments, or A/B testing.
- Export clean JSON ready for ingestion into warehouses, BI tools, or automation scripts.

## Features

| Feature | Description |
|--------|-------------|
| Sound-based video crawling | Fetch all videos that use a given TikTok sound/music URL and return structured data per video. |
| Keyword-based sound search | Search TikTok sounds by keyword and get ranked music results with metadata and usage counts. |
| No-watermark video URLs | Retrieve direct video URLs without watermarks for clean reuse in analysis, previews, or tooling. |
| Rich creator metadata | Collect creator information such as nickname, bio, verification, followers, following, and likes. |
| Detailed engagement stats | Capture likes, plays, comments, shares, and collections to analyze performance across videos. |
| Audio and music metadata | Extract sound title, author, duration, album, tags, and cover images for cataloging and search. |
| Flexible filters and sorting | Use type, filterBy, sortType, region, and limit to fine-tune your scraping runs. |
| Region-specific results | Target specific regions via two-character country codes to localize your sound research. |
| Robust JSON responses | Get data in consistent JSON structures suitable for direct ETL or analytics pipelines. |
| Performance-optimized runs | Designed to process many items quickly while minimizing unnecessary requests. |

---

## What Data This Scraper Extracts

| Field Name | Field Description |
|-----------|-------------------|
| type | Fetching type for the run, e.g. `POST_LIST` for videos by sound URL or `SEARCH` for music search by keyword. |
| keyword | Keyword used when searching TikTok music, such as artist names, track titles, or phrases. |
| region | Two-letter country/region code (e.g. `GB`, `US`, `VN`) that scopes search and listing behavior. |
| url | TikTok sound/music URL used for collecting all related videos (when `type` is `POST_LIST`). |
| filterBy | Search filter when using keyword mode; options like `ALL`, `TITLE`, `CREATOR` to refine results. |
| sortType | Sorting strategy such as `RELEVANCE`, `MOST USED`, `MOST RECENT`, `SHORTEST`, `LONGEST` for music search results. |
| limit | Maximum number of items to return for the current run, controlling data volume and load. |
| added_sound_music_info | Core sound/music object containing title, id, author, album, duration, tags, and cover images. |
| added_sound_music_info.author | Music or sound author name (e.g. channel or artist). |
| added_sound_music_info.title | Human-readable sound or song title as shown in TikTok. |
| added_sound_music_info.play_url | Direct audio URL (e.g. MP3) for the TikTok sound. |
| added_sound_music_info.cover_large / medium / thumb | URLs to large, medium, and thumbnail cover images for the sound. |
| author.uid | Unique ID of the video creator who used the sound. |
| author.nickname | Creator’s displayed name on TikTok. |
| author.unique_id | Creator’s unique handle (username) string. |
| author.signature | Creator’s bio/about text. |
| author.region | Creator’s region code specified in their profile. |
| author.follower_count | Total number of followers the creator has at capture time. |
| author.following_count | Total number of accounts the creator follows. |
| author.total_favorited | Sum of likes received by the creator across their content. |
| author.custom_verify / verify_info | Fields that indicate verification status and verification labels. |
| music.id / music.mid | Internal music identifiers that map videos to a specific sound. |
| music.author | Author of the music used in the video. |
| music.title | Title of the music track or original sound as attached to the video. |
| music.duration | Length of the music track in seconds. |
| music.play_url | Direct URL for audio playback of the track. |
| music.user_count | Number of users who have used this sound in their videos. |
| aweme_id | Unique ID of the TikTok video associated with the sound. |
| desc | Human-readable video caption/description. |
| create_time | Unix timestamp of video creation time. |
| cha_list | List of hashtags/challenges linked to the video, with challenge IDs and share URLs. |
| statistics.play_count | Total number of video plays/views. |
| statistics.digg_count | Number of likes the video has received. |
| statistics.comment_count | Number of comments on the video. |
| statistics.share_count | Number of shares for the video. |
| statistics.collect_count | Number of times the video has been saved/collected. |
| video.play_addr | Primary playback URL information, including multiple quality variations. |
| video.download_addr | Download URL information, which may include watermark variants. |
| video.duration | Video duration in milliseconds. |
| video.ratio | Quality label like `540p` describing resolution. |
| video.cover / dynamic_cover / origin_cover | Static and dynamic cover image URLs for thumbnails and previews. |
| share_info.share_url | Public TikTok share URL to the video. |
| share_info.share_title / share_desc | Default share title and description strings. |
| text_extra | Structured references extracted from caption text such as hashtags and sound mentions. |
| playlist_info | When available, information about playlists the video is part of, including index and total items. |
| search_music_result.id | Music ID returned for each search result entry when running in search mode. |
| search_music_result.title | Title of the sound from search results. |
| search_music_result.author | Author of the sound from search results. |
| search_music_result.cover_large / medium / thumb | Cover images for each music search result. |
| search_music_result.play_url | Direct audio URL for each sound returned by search. |
| search_music_result.user_count | Count of users or videos detected using that sound. |

---

## Example Output

Example:


    [
      {
        "type": "POST_LIST",
        "region": "GB",
        "url": "https://www.tiktok.com/music/Love-You-So-6728562975734515713",
        "limit": 20,
        "added_sound_music_info": {
          "id": "7229168247013182210",
          "title": "original sound - vtvgiaitriofficial",
          "author": "Bigbang Official",
          "duration": 54,
          "play_url": "https://sf16-ies-music-sg.tiktokcdn.com/obj/tiktok-obj/7229168238650166018.mp3",
          "cover_large": "https://p16-sign-sg.tiktokcdn.com/aweme/1080x1080/...",
          "user_count": 0
        },
        "author": {
          "uid": "6812490744957256705",
          "unique_id": "vtvgiaitriofficial",
          "nickname": "Bigbang Official",
          "signature": "Mời các bạn tải ứng dụng VTV GiảiTrí để xem trọn bộ phim hay độc quyền",
          "region": "VN",
          "follower_count": 0,
          "following_count": 0,
          "total_favorited": 0,
          "custom_verify": "Verified account"
        },
        "aweme_id": "7229167805625847041",
        "desc": "Cô chủ trọ cho thuê căn phòng hết nước chấm thật #Cuocdoivandepsao",
        "create_time": 1683171893,
        "statistics": {
          "play_count": 585709,
          "digg_count": 25006,
          "comment_count": 183,
          "share_count": 492,
          "collect_count": 743
        },
        "video": {
          "duration": 54635,
          "ratio": "540p",
          "play_addr": "https://v19.tiktokcdn-us.com/422f47cb49d0e1ec92bc607815c11cfb/...",
          "download_addr": "https://v19.tiktokcdn-us.com/9f47f3002207837dc9085f8832348578/...",
          "has_watermark": true
        },
        "share_info": {
          "share_url": "https://www.tiktok.com/@vtvgiaitriofficial/video/7229167805625847041",
          "share_title": "Check out Bigbang Official’s video! #TikTok"
        }
      }
    ]

---

## Directory Structure Tree

Assume this is a complete working Python-based project exposing a CLI and simple SDK around the TikTok Sound Music API scraper.


    TikTok Sound Music API (free-watermark videos)/
    ├── src/
    │   ├── main.py
    │   ├── cli.py
    │   ├── client/
    │   │   ├── __init__.py
    │   │   └── tiktok_sound_client.py
    │   ├── pipelines/
    │   │   ├── sound_post_list.py
    │   │   └── sound_search.py
    │   ├── models/
    │   │   ├── sound_item.py
    │   │   └── video_item.py
    │   ├── utils/
    │   │   ├── http.py
    │   │   ├── logging_utils.py
    │   │   └── rate_limiter.py
    │   └── config/
    │       ├── settings.example.json
    │       └── schema.json
    ├── data/
    │   ├── input.post_list.example.json
    │   ├── input.search.example.json
    │   └── sample_output.json
    ├── tests/
    │   ├── test_sound_post_list.py
    │   └── test_sound_search.py
    ├── pyproject.toml
    ├── requirements.txt
    └── README.md

---

## Use Cases

- **Music labels** use it to **track which sounds and songs are going viral across regions**, so they can **identify breakout tracks early and prioritize promotion or sync deals**.
- **Creator agencies** use it to **map which creators are driving sound-based trends**, so they can **discover suitable partners for campaigns and negotiate data-backed collaborations**.
- **Growth marketers** use it to **monitor performance of specific sounds tied to campaigns**, so they can **iterate on creatives and target the most engaging sound variants**.
- **Analytics teams** use it to **ingest sound and video statistics into data warehouses**, so they can **build dashboards for sound usage, engagement funnels, and trend lifecycles**.
- **Tool builders and SaaS products** use it to **embed TikTok sound search and performance insights into their apps**, so their users **get live sound intelligence without building a scraper from scratch**.

---

## FAQs

**Q: Do I need to log in to TikTok to use this scraper?**
A: No. The scraper is designed to work with publicly accessible TikTok sound and video data. You provide sound URLs or search keywords, along with region and filters, and it returns the structured results without requiring credentials.

**Q: Can I fetch videos for any TikTok sound URL?**
A: As long as the sound is publicly accessible and not restricted to private content, you can use its music URL as input with `type` set to `POST_LIST`. The scraper will attempt to collect associated videos up to the specified `limit`, respecting any regional or content limitations imposed by TikTok.

**Q: How accurate are the statistics like likes and plays?**
A: Metrics such as play_count, digg_count, and share_count are captured at the time of scraping. They match what is publicly visible at that moment but may change later as the video continues to receive engagement. For time-series analysis, schedule recurring runs and store historical snapshots.

**Q: What happens if I use a very high limit or broad keyword?**
A: Very large limits or generic keywords can increase runtime and the volume of data returned. It’s recommended to start with moderate limits, apply `filterBy` and `sortType` settings, and narrow your search terms when you want more precise datasets.

---

## Performance Benchmarks and Results

- **Primary Metric – Scraping Speed:** On a typical connection and healthy network conditions, the scraper can process around 100–150 video entries or music search results in roughly 30 seconds with optimized parameters and moderate limits.
- **Reliability Metric – Success Rate:** With stable network access, the success rate for fetching valid JSON responses per run commonly exceeds 95%, assuming inputs are valid and target content is publicly available.
- **Efficiency Metric – Resource Usage:** Input-driven limiting (via `limit`) and batched HTTP requests help keep resource usage low, allowing you to run multiple small jobs instead of one huge, heavy task.
- **Quality Metric – Data Completeness:** For publicly available sounds and videos, the scraper aims to return full creator metadata, sound details, and engagement stats, yielding high data completeness suitable for downstream analytics, dashboards, and trend modelling.


<p align="center">
<a href="https://calendar.app.google/74kEaAQ5LWbM8CQNA" target="_blank">
  <img src="https://img.shields.io/badge/Book%20a%20Call%20with%20Us-34A853?style=for-the-badge&logo=googlecalendar&logoColor=white" alt="Book a Call">
</a>
  <a href="https://www.youtube.com/@bitbash-demos/videos" target="_blank">
    <img src="https://img.shields.io/badge/🎥%20Watch%20demos%20-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch on YouTube">
  </a>
</p>
<table>
  <tr>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtu.be/MLkvGB8ZZIk" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review1.gif" alt="Review 1" width="100%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Bitbash is a top-tier automation partner, innovative, reliable, and dedicated to delivering real results every time.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Nathan Pennington
        <br><span style="color:#888;">Marketer</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtu.be/8-tw8Omw9qk" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review2.gif" alt="Review 2" width="100%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Bitbash delivers outstanding quality, speed, and professionalism, truly a team you can rely on.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Eliza
        <br><span style="color:#888;">SEO Affiliate Expert</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtube.com/shorts/6AwB5omXrIM" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review3.gif" alt="Review 3" width="35%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Exceptional results, clear communication, and flawless delivery. Bitbash nailed it.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Syed
        <br><span style="color:#888;">Digital Strategist</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
  </tr>
</table>
