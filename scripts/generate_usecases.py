#!/usr/bin/env python3
"""
Generate 200 n8n use cases, each with:
  - usecases/NN-<slug>/Dockerfile
  - usecases/NN-<slug>/README.md  (with Mermaid diagram)
plus the main README index table with GitHub Dockerfile links.

Run:  python3 scripts/generate_usecases.py
"""

import os
import re

REPO = "https://github.com/rahuleraser/AI_Agent_LLM_011_n8n"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UC_ROOT = os.path.join(ROOT, "usecases")

# ---------------------------------------------------------------------------
# Data model per use case:
#   num        - int
#   title      - display title
#   category   - market category
#   desc       - short description
#   trigger    - diagram: trigger node label
#   step1      - diagram: fetch / normalize step
#   step2      - diagram: process step
#   condition  - diagram: IF decision
#   action_yes - diagram: yes branch
#   action_no  - diagram: no branch
#   output     - diagram: notify / store output
#   community  - list of verified npm community node packages
#   env        - list of "KEY=value" use-case specific env defaults
#   nodes      - list of "Node|Purpose" rows for the key nodes table
# ---------------------------------------------------------------------------

# fmt: off
UC = [
# =========================== 01-15 Email & Communication =====================
(1,"Gmail Inbox Processor","Email & Communication","Processes incoming Gmail, classifies mail and logs every action to a spreadsheet.","Gmail Trigger (New Email)","Read Email Body and Sender","Classify with IF / Keywords","IF: Important sender?","Send Reply with Template","Archive and Label Email","Log to Google Sheets",
 ["n8n-nodes-sqlite"],["WEBHOOK_PATH=email-process","POLL_MINUTES=15"],["Gmail Trigger|Fires on new email","Gmail|Reads body and sender","IF|Classifies mail type","Gmail Send|Replies with template","Google Sheets|Logs every action","SQLite|Stores audit history"]),
(2,"Gmail Auto-Responder","Email & Communication","Automatically replies to common emails with templates based on detected intent.","Gmail Trigger (Unread)","Detect Intent (Keywords)","Pick Template by Intent","IF: Needs human review?","Send Template Reply","Forward to Support Team","Flag as Handled",
 [],["WEBHOOK_PATH=auto-respond","REPLY_LIMIT_DAILY=50"],["Gmail Trigger|Listens for unread","Code|Detects intent","Switch|Selects template","Gmail Send|Replies automatically","Gmail|Forwards edge cases","Spreadsheet|Tracks replies"]),
(3,"Email Digest Builder","Email & Communication","Aggregates daily emails and compiles a single morning summary digest.","Cron Trigger (Daily 8am)","Fetch Unread Emails","Rank by Importance","IF: Contains action item?","Add to Action List","Add to Read-Only List","Send Digest Email",
 [],["CRON_SCHEDULE=0 8 * * 1-5","DIGEST_MAX_EMAILS=20"],["Cron Trigger|Scheduled daily run","Gmail|Fetches emails","Code|Scores importance","IF|Splits action items","Email Send|Delivers digest","Spreadsheet|Stores digest log"]),
(4,"Email Forwarding Router","Email & Communication","Routes inbound emails to the right department mailbox based on subject rules.","Gmail Trigger (Inbound)","Parse Recipient and Subject","Match Routing Rules","IF: Sales related?","Forward to Sales Mailbox","Forward to Support Mailbox","Log Routing Decision",
 [],["WEBHOOK_PATH=email-route","ROUTE_TABLE=json"],["Gmail Trigger|Inbound hook","Code|Extracts fields","Switch|Applies rules","Gmail Send|Forwards mail","IF|Fallback routing","SQLite|Route history"]),
(5,"Email Attachment Saver","Email & Communication","Saves email attachments to cloud storage and records metadata in a sheet.","Gmail Trigger (Attachment)","List Attachments","Upload to Drive / S3","IF: File too large?","Compress File","Upload as-is","Log Metadata to Sheet",
 ["n8n-nodes-mongodb"],["WEBHOOK_PATH=attachment-save","MAX_FILE_MB=25"],["Gmail Trigger|Fires on attachment","Code|Lists files","Google Drive|Stores files","S3|Stores files","IF|Size check","MongoDB|Metadata archive"]),
(6,"Cold Email Outreach","Email & Communication","Sends a personalized cold outreach sequence to a lead list with follow-ups.","Spreadsheet Trigger (Lead List)","Format Personalized Email","Wait N Days","IF: Got a reply?","Stop Sequence","Send Follow-up","Mark Status in Sheet",
 [],["OUTREACH_STEP_WAIT_DAYS=3","MAX_FOLLOWUPS=3"],["Spreadsheet File|Reads leads","Email Send|Sends first email","Wait|Adds delay","Gmail|Checks replies","IF|Branches sequence","Spreadsheet|Tracks status"]),
(7,"Newsletter Subscriber Manager","Email & Communication","Manages newsletter subscribers and sends a weekly issue automatically.","Webhook (Subscribe Form)","Add to Subscriber List","Send Welcome Email","IF: Unsubscribed?","Remove from List","Send Weekly Issue","Log Stats",
 [],["WEBHOOK_PATH=subscribe","WEEKLY_CRON=0 9 * * 3"],["Webhook|Subscriber signup","Email Send|Welcome mail","Cron Trigger|Weekly send","Email Send|Issue delivery","IF|Handles unsubscribes","Spreadsheet|Stats log"]),
(8,"Email Bounce Handler","Email & Communication","Processes hard bounces and auto-removes invalid addresses from lists.","Email Webhook (Bounce)","Classify Bounce Type","IF: Hard or Soft?","Remove Address from List","Retry with Backoff","Update List Status","Notify List Owner",
 ["n8n-nodes-sqlite"],["WEBHOOK_PATH=bounce","RETRY_BACKOFF_HOURS=24"],["Webhook|Bounce event","Code|Classifies bounce","IF|Hard vs soft","Email Send|Retry logic","Spreadsheet|List updates","SQLite|Bounce history"]),
(9,"Email Unsubscribe Processor","Email & Communication","Processes unsubscribe requests and confirms removal across all lists.","Email Trigger (Unsubscribe)","Extract Email Address","Remove from All Lists","IF: Confirmation needed?","Send Confirmation Email","Update Records","Log Unsubscribe",
 [],["WEBHOOK_PATH=unsubscribe","LISTS=newsletter,alerts"],["Email Trigger|Detects request","Code|Extracts address","Email Send|Confirms removal","Spreadsheet|Updates lists","IF|Confirmation flow","SQLite|Unsubscribe log"]),
(10,"Calendar Invite Sync","Email & Communication","Reads calendar invites from email and creates matching calendar events.","Gmail Trigger (Calendar Invite)","Parse Invite Details","Create Calendar Event","IF: Conflicts found?","Notify Organizer","Create Event + Reminder","Sync to Sheet",
 [],["WEBHOOK_PATH=cal-invite","REMINDER_MINUTES=15"],["Gmail Trigger|Invite email","Code|Parses .ics","Google Calendar|Creates event","IF|Conflict check","Email|Notifies organizer","Google Sheets|Sync log"]),
(11,"Slack Message Relay","Email & Communication","Relays messages between email and Slack channels automatically.","Slack Trigger (Channel)","Detect Email Request","Send Email via SMTP","IF: Action required?","Post to Support Channel","Acknowledge to Slack","Log Relay",
 [],["WEBHOOK_PATH=slack-relay","SLACK_CHANNEL=general"],["Slack Trigger|Channel events","Code|Detects intent","Email Send|Outbound mail","IF|Routes to channel","Slack|Sends message","Spreadsheet|Relay log"]),
(12,"Slack Channel Moderator","Email & Communication","Monitors Slack channels and alerts moderators about flagged messages.","Slack Trigger (New Message)","Scan for Flags","IF: Contains spam?","Post Alert to Moderators","Ignore Message","Remove Message","Notify Sender",
 [],["FLAG_KEYWORDS=spam,scam,urgent"],["Slack Trigger|New message","Code|Flag scan","IF|Spam decision","Slack|Moderator alert","Slack|Removes message","SQLite|Flag history"]),
(13,"Slack Standup Reminder","Email & Communication","Posts daily standup prompts and collects team updates in one thread.","Cron Trigger (Daily 9am)","Build Standup Prompt","Post to Slack Thread","IF: Replies collected?","Compile Update Summary","Remind Again","Save to Sheet",
 [],["STANDUP_CRON=0 9 * * 1-5","STANDUP_CHANNEL=team"],["Cron Trigger|Daily prompt","Slack|Posts prompt","Wait|Collects replies","Code|Compiles summary","IF|Completion check","Google Sheets|Stores updates"]),
(14,"Discord Announcement Bot","Email & Communication","Posts announcements to Discord communities on a schedule or on demand.","Cron / Webhook Trigger","Format Announcement","IF: Has image?","Post with Embed Image","Post Text Only","Post to Discord Channel","Log Announcements",
 ["n8n-nodes-discord"],["ANNOUNCE_CRON=0 10 * * *","DISCORD_CHANNEL=announcements"],["Cron Trigger|Schedule","Code|Formats message","Discord|Posts embed","IF|Image branch","Discord|Text-only post","SQLite|Announcement log"]),
(15,"SMS Order Notification","Email & Communication","Sends SMS order updates to customers after order events.","Order Webhook","Build SMS Content","IF: Order shipped?","Send Shipping SMS","Send Processing SMS","Send Delivery SMS","Log SMS Status",
 [],["SMS_WEBHOOK_PATH=order-sms","SMS_PROVIDER=twilio"],["Webhook|Order event","Code|Builds message","IF|Status branch","Twilio|Sends SMS","Spreadsheet|Order state","SQLite|SMS log"]),
# =========================== 16-35 Social Media & Marketing ==================
(16,"Twitter Auto-Reply","Social Media & Marketing","Replies to Twitter mentions automatically with helpful answers.","Twitter Trigger (Mention)","Analyze Tweet Intent","Build Reply Text","IF: Needs escalation?","DM Support Team","Post Public Reply","Log Interactions",
 [],["TWITTER_WEBHOOK_PATH=tw-reply"],["Twitter Trigger|Mentions","Code|Intent analysis","Twitter|Public reply","IF|Escalation branch","Slack|Alerts support","SQLite|Interaction log"]),
(17,"Twitter Thread Publisher","Social Media & Marketing","Publishes a multi-tweet thread from a spreadsheet of tweets.","Spreadsheet Trigger (Thread)","Load Tweets in Order","IF: Validate each tweet?","Publish Tweet Sequentially","Flag Invalid Tweet","Wait Between Tweets","Log Published Thread",
 [],["THREAD_WAIT_SECONDS=30","TWEET_LIMIT_CHARS=280"],["Spreadsheet File|Tweet list","Code|Validates tweets","Twitter|Publishes tweet","Wait|Spacing delay","IF|Validation branch","Spreadsheet|Publish log"]),
(18,"Facebook Page Poster","Social Media & Communication","Posts scheduled content to a Facebook page with images.","Cron Trigger (Schedule)","Fetch Content from Sheet","Build Post Payload","IF: Has media?","Post with Photo","Post Text Only","Log Post Result",
 [],["FB_POST_CRON=0 12 * * *","FB_PAGE_ID=your-page"],["Cron Trigger|Schedule","Google Sheets|Content source","Facebook|Creates post","IF|Media branch","Facebook|Photo post","Spreadsheet|Post log"]),
(19,"Instagram Content Scheduler","Social Media & Marketing","Schedules Instagram posts with images and captions.","Spreadsheet Trigger (Content)","Prepare Image + Caption","IF: Business account?","Schedule via Graph API","Flag Account Type","Publish Post","Log Schedule",
 [],["INSTAGRAM_WEBHOOK_PATH=ig-post"],["Spreadsheet File|Content plan","Code|Prepares media","Instagram|Publishes post","IF|Account check","Spreadsheet|Schedule log","Code|Caption format"]),
(20,"LinkedIn Article Publisher","Social Media & Marketing","Cross-publishes blog content to LinkedIn as articles.","RSS Trigger (New Blog Post)","Extract Article Content","Convert to LinkedIn Format","IF: Content too long?","Trim and Publish","Publish Full Article","Log Publishing",
 [],["LINKEDIN_WEBHOOK_PATH=li-publish"],["RSS Trigger|New post","Code|Extracts content","LinkedIn|Publishes article","IF|Length check","Spreadsheet|Publish log","Code|Formatting"]),
(21,"YouTube New Video Notifier","Social Media & Marketing","Detects new YouTube uploads and notifies the community.","YouTube Trigger (New Video)","Fetch Video Details","Build Notification","IF: Category matches?","Post to Discord","Post to Telegram","Log Notifications",
 ["n8n-nodes-telegram","n8n-nodes-discord"],["YOUTUBE_CHANNEL=your-channel"],["YouTube Trigger|New upload","HTTP Request|Video metadata","Discord|Channel post","Telegram|Direct message","IF|Category filter","SQLite|Notification log"]),
(22,"TikTok Trend Watcher","Social Media & Marketing","Watches TikTok hashtags and collects trending video insights.","Cron Trigger (Hourly)","Query Hashtag Feed","Collect Video Stats","IF: Above threshold?","Save to Trend Sheet","Skip Video","Notify Marketer",
 [],["TT_TREND_CRON=0 * * * *","TT_HASHTAG=trending"],["Cron Trigger|Polling","HTTP Request|TikTok API","Code|Collects stats","IF|Threshold check","Google Sheets|Trend store","Slack|Marketer alert"]),
(23,"Pinterest Pin Scheduler","Social Media & Marketing","Schedules pins from a content board to Pinterest.","Spreadsheet Trigger (Pins)","Fetch Pin Image and Link","Build Pin Metadata","IF: Valid image?","Schedule Pin","Flag Broken Image","Log Pin Status",
 [],["PINTEREST_WEBHOOK_PATH=pin-schedule"],["Spreadsheet File|Pin list","Code|Prepares pin","Pinterest|Creates pin","IF|Image validation","Spreadsheet|Pin status","Code|Metadata build"]),
(24,"Reddit Post Monitor","Social Media & Marketing","Tracks Reddit mentions of your brand and routes them to the team.","Reddit Trigger (New Post)","Classify Post Sentiment","IF: Brand mentioned?","Notify Community Manager","Log to Monitor Sheet","Reply if Needed","Score Sentiment",
 [],["REDDIT_WEBHOOK_PATH=reddit-monitor","BRAND_KEYWORDS=yourbrand"],["Reddit Trigger|New posts","Code|Sentiment score","IF|Brand mention","Slack|Community alert","Google Sheets|Monitor log","Code|Reply draft"]),
(25,"Social Mention Tracker","Social Media & Marketing","Monitors brand mentions across social platforms in one dashboard.","Cron Trigger (30 min)","Query Mention APIs","Aggregate Mentions","IF: Sentiment negative?","Alert Team","Store Mention","Update Dashboard",
 [],["MENTION_CRON=*/30 * * * *","BRAND_NAME=yourbrand"],["Cron Trigger|Polling","HTTP Request|Multiple APIs","Code|Aggregates mentions","IF|Negative flag","Slack|Team alert","Google Sheets|Dashboard"]),
(26,"Hashtag Performance Reporter","Social Media & Marketing","Reports which hashtags drive the most engagement per week.","Cron Trigger (Weekly)","Collect Post Metrics","Group by Hashtag","IF: Metric improved?","Add to Winner List","Keep in Watch List","Email Performance Report",
 [],["HASHTAG_CRON=0 9 * * 1","TRACKED_HASHTAGS=#brand,#launch"],["Cron Trigger|Weekly run","HTTP Request|Post metrics","Code|Groups hashtags","IF|Improvement check","Email|Sends report","Google Sheets|Trend data"]),
(27,"Influencer Outreach","Social Media & Marketing","Automates influencer outreach and tracks campaign responses.","Spreadsheet Trigger (Influencers)","Personalize Outreach DM","IF: Reply received?","Add to Campaign","Send Follow-up","Update Status","Notify Campaign Manager",
 [],["INFLUENCER_WAIT_DAYS=2","CAMPAIGN_ID=your-campaign"],["Spreadsheet File|Influencer list","Email/DM|Outreach","IF|Reply detection","Spreadsheet|Status update","Slack|Campaign alert","Code|Personalization"]),
(28,"Social Media Reposting","Social Media & Marketing","Cross-posts content between platforms to maximize reach.","Webhook (New Content)","Normalize Content","IF: Platform supported?","Repost to Targets","Skip Platform","Log Cross-post","Notify Poster",
 [],["REPOST_WEBHOOK_PATH=repost"],["Webhook|Content event","Code|Normalizes content","Switch|Target platforms","IF|Support check","Social APIs|Cross-post","Spreadsheet|Repost log"]),
(29,"Viral Content Curator","Social Media & Marketing","Curates trending content from sources and schedules reposts.","RSS / Cron Trigger","Fetch Trending Items","Score Viral Potential","IF: Score high?","Queue for Posting","Archive Item","Notify Curator",
 [],["CURATE_CRON=0 6 * * *","MIN_VIRAL_SCORE=70"],["RSS Trigger|Trending feed","Code|Scores content","IF|High-score queue","Spreadsheet|Posting queue","Slack|Curator alert","Code|Archive logic"]),
(30,"Social Media Ad Monitor","Social Media & Marketing","Monitors ad campaign budgets and performance across platforms.","Cron Trigger (Daily)","Pull Ad Spend Metrics","IF: Spend over budget?","Alert Marketing Team","Log Performance","Pause Underperforming Ads","Email Daily Summary",
 [],["AD_MONITOR_CRON=0 8 * * *","AD_BUDGET=100"],["Cron Trigger|Daily pull","Facebook Ads API|Metrics","IF|Budget check","Slack|Marketing alert","Facebook Ads|Pause action","Email|Summary report"]),
(31,"Brand Sentiment Monitor","Social Media & Marketing","Tracks brand sentiment on social media and reports trends.","Cron Trigger (Hourly)","Collect Social Mentions","Analyze Sentiment","IF: Sentiment shift?","Generate Alert","Update Scoreboard","Email Weekly Sentiment",
 [],["SENTIMENT_CRON=0 * * * *","BRAND_ALIAS=yourbrand"],["Cron Trigger|Collection","HTTP Request|Mention APIs","AI|Sentiment analysis","IF|Shift detection","Google Sheets|Scoreboard","Email|Weekly report"]),
(32,"Social Poll Collector","Social Media & Marketing","Collects poll responses from social platforms and analyzes results.","Social Trigger (Poll Response)","Capture Response","IF: Poll closed?","Compile Results","Record Vote","Publish Result Post","Log to Sheet",
 [],["POLL_WEBHOOK_PATH=poll-vote"],["Social Trigger|Poll events","Code|Captures votes","IF|Closure check","Google Sheets|Vote log","Social API|Publishes result","Code|Compiles results"]),
(33,"Social Contest Handler","Social Media & Marketing","Runs giveaways, picks winners and notifies participants automatically.","Webhook (Entry)","Collect Entries","IF: Contest ended?","Pick Random Winner","Store Entry","Notify Winner","Log Contest Results",
 [],["CONTEST_WEBHOOK_PATH=contest-entry"],["Webhook|Entry capture","Code|Entry store","Cron Trigger|End date","Code|Random pick","Social API|Winner DM","Spreadsheet|Results log"]),
(34,"Community Reward Auto-sender","Social Media & Marketing","Automatically sends rewards to community members who complete actions.","Webhook (Action Completed)","Verify Action","IF: Reward eligible?","Send Reward Code","Log Attempt","Notify Member","Update Points Ledger",
 ["n8n-nodes-sqlite"],["REWARD_WEBHOOK_PATH=reward"],["Webhook|Action event","Code|Verifies action","IF|Eligibility check","Email|Sends reward","SQLite|Ledger","Slack|Admin log"]),
(35,"Social Profile Health Check","Social Media & Marketing","Checks all social profiles for issues like broken links or missing info.","Cron Trigger (Monthly)","Fetch Profile Fields","Validate Against Checklist","IF: Issue found?","Create Fix Task","Mark Healthy","Email Health Report",
 [],["PROFILE_CRON=0 9 1 * *","CHECKLIST_URL=sheet-link"],["Cron Trigger|Monthly scan","HTTP Request|Profile data","Code|Checklist checks","IF|Issue detection","Google Sheets|Fix tasks","Email|Health report"]),
# =========================== 36-50 E-commerce & Retail =======================
(36,"Shopify New Order Alert","E-commerce & Retail","Alerts the team instantly when a new Shopify order is placed.","Shopify Trigger (New Order)","Fetch Order Details","Build Alert Message","IF: High value order?","VIP Channel Alert","Standard Channel Alert","Log Order Event",
 [],["SHOPIFY_WEBHOOK_PATH=shopify-order","VIP_ORDER_VALUE=500"],["Shopify Trigger|New order","HTTP Request|Order details","Code|Alert formatting","IF|VIP threshold","Slack|Channel alerts","Spreadsheet|Order log"]),
(37,"Shopify Inventory Sync","E-commerce & Retail","Syncs inventory levels between Shopify and a local database.","Cron Trigger (Hourly)","Fetch Product Inventory","IF: Stock changed?","Update Database","Skip Product","Alert Low Stock","Log Sync",
 ["n8n-nodes-sqlite"],["INV_CRON=0 * * * *","LOW_STOCK_THRESHOLD=5"],["Cron Trigger|Polling","Shopify|Inventory API","IF|Change detection","SQLite|Stock store","IF|Low stock check","Slack|Inventory alert"]),
(38,"Shopify Refund Processor","E-commerce & Retail","Automates refund workflows and logs refund status to finance.","Shopify Trigger (Refund)","Fetch Refund Details","IF: Refund valid?","Process Refund","Flag for Review","Update Finance Sheet","Notify Customer",
 ["n8n-nodes-stripe"],["REFUND_WEBHOOK_PATH=refund"],["Shopify Trigger|Refund event","Code|Validates refund","Stripe|Processes refund","IF|Validation branch","Google Sheets|Finance log","Email|Customer notice"]),
(39,"WooCommerce Order Fetcher","E-commerce & Retail","Imports new WooCommerce orders into a central spreadsheet.","WooCommerce Trigger (Order)","Fetch Order Items","Normalize Fields","IF: Duplicate order?","Skip Import","Append to Sheet","Notify Team",
 [],["WOO_WEBHOOK_PATH=woo-order"],["WooCommerce Trigger|New order","HTTP Request|Order data","Code|Normalizes fields","IF|Duplicate check","Google Sheets|Order ledger","Slack|Team notice"]),
(40,"E-commerce Price Monitor","E-commerce & Retail","Monitors competitor prices and alerts when thresholds are crossed.","Cron Trigger (Daily)","Scrape Product Pages","Extract Prices","IF: Price below target?","Alert Pricing Team","Store Price","Update Price Tracker",
 [],["PRICE_CRON=0 7 * * *","PRICE_TARGET=49.99"],["Cron Trigger|Daily scrape","HTTP Request|Product pages","Code|Extracts price","IF|Threshold check","Slack|Pricing alert","Google Sheets|Price tracker"]),
(41,"Product Review Collector","E-commerce & Retail","Collects product reviews from multiple platforms into one place.","Cron Trigger (Daily)","Fetch New Reviews","IF: Review rating low?","Alert Support Team","Add to Review DB","Reply to Reviewer","Update Review Dashboard",
 ["n8n-nodes-mongodb"],["REVIEW_CRON=0 6 * * *","LOW_RATING=2"],["Cron Trigger|Review pull","HTTP Request|Platform APIs","IF|Low rating flag","MongoDB|Review store","Email|Reply drafting","Google Sheets|Dashboard"]),
(42,"Amazon Price Tracker","E-commerce & Retail","Tracks Amazon product prices and alerts on drops.","Cron Trigger (Hourly)","Fetch Amazon Price","Compare with History","IF: Price dropped?","Send Drop Alert","Update Price History","Log Change",
 ["n8n-nodes-sqlite"],["AMZ_PRICE_CRON=0 * * * *","ASIN_LIST=A1B2C3D4E5"],["Cron Trigger|Hourly poll","HTTP Request|Product data","Code|Price compare","IF|Drop detection","Email|Drop alert","SQLite|Price history"]),
(43,"eBay Listing Sync","E-commerce & Retail","Syncs eBay listings with inventory counts in real time.","eBay Trigger (Listing)","Fetch Listing Data","IF: Quantity changed?","Update Inventory","Log Listing","Alert Low Quantity","Sync to Sheet",
 [],["EBAY_WEBHOOK_PATH=ebay-sync"],["eBay Trigger|Listing event","eBay API|Listing data","IF|Quantity check","SQLite|Inventory store","Google Sheets|Sync log","Slack|Low stock alert"]),
(44,"Etsy Order Processor","E-commerce & Retail","Processes Etsy orders and sends confirmation emails automatically.","Etsy Trigger (New Order)","Fetch Order Details","Generate Confirmation","IF: Digital item?","Send Digital Link","Send Shipping Update","Log Order",
 [],["ETSY_WEBHOOK_PATH=etsy-order"],["Etsy Trigger|New order","HTTP Request|Order details","Email|Confirmation","IF|Item type branch","Email|Digital delivery","Spreadsheet|Order log"]),
(45,"Magento Order Sync","E-commerce & Retail","Syncs Magento orders to accounting and fulfillment tools.","Magento Trigger (Order)","Fetch Order Payload","IF: Payment received?","Create Fulfillment Task","Flag Unpaid Order","Update Accounting Sheet","Notify Ops Team",
 [],["MAGENTO_WEBHOOK_PATH=magento-order"],["Magento Trigger|Order event","HTTP Request|Order data","IF|Payment check","Google Sheets|Fulfillment","Google Sheets|Accounting","Slack|Ops alert"]),
(46,"BigCommerce Abandoned Cart","E-commerce & Retail","Recovers abandoned carts with automated email nudges.","BigCommerce Trigger (Cart)","Fetch Cart Contents","IF: Cart abandoned?","Send Recovery Email","Ignore Active Cart","Apply Discount Code","Log Recovery",
 [],["BIGCART_WEBHOOK_PATH=cart-abandon","ABANDON_WAIT_HOURS=24"],["BigCommerce Trigger|Cart event","HTTP Request|Cart data","IF|Abandon check","Email|Recovery email","Code|Discount code","Spreadsheet|Recovery log"]),
(47,"Subscription Renewal Reminder","E-commerce & Retail","Reminds customers about upcoming subscription renewals.","Cron Trigger (Daily)","Find Renewals Due","IF: Within 3 days?","Send Reminder Email","Skip Subscription","Update Renewal Log","Notify Billing Team",
 [],["RENEWAL_CRON=0 9 * * *","RENEW_WINDOW_DAYS=3"],["Cron Trigger|Daily check","SQLite|Subscriptions","IF|Window check","Email|Reminder send","Google Sheets|Renewal log","Slack|Billing alert"]),
(48,"Dropshipping Order Router","E-commerce & Retail","Routes dropship orders to the correct supplier automatically.","Shopify Trigger (Order)","Match Product to Supplier","IF: Supplier found?","Send Order to Supplier","Flag Manual Handling","Log Routing","Notify Supplier",
 [],["DROPSHIP_WEBHOOK_PATH=dropship-route"],["Shopify Trigger|New order","Code|Supplier match","IF|Match check","Email|Supplier order","Google Sheets|Routing log","Slack|Manual flag"]),
(49,"Marketplace Feedback Request","E-commerce & Retail","Requests reviews from buyers after successful deliveries.","Order Trigger (Delivered)","Build Feedback Request","IF: Eligible for review?","Send Feedback Email","Skip Buyer","Wait for Reply","Log Requests",
 [],["FEEDBACK_WAIT_DAYS=7"],["Order Trigger|Delivery event","Code|Eligibility check","IF|Review eligibility","Email|Feedback request","Wait|Reply window","Spreadsheet|Request log"]),
(50,"E-commerce Customer Win-back","E-commerce & Retail","Re-engages lapsed customers with targeted offers.","Cron Trigger (Weekly)","Find Inactive Customers","Segment by Spend","IF: High value customer?","Send VIP Offer","Send Standard Offer","Log Campaign",
 [],["WINBACK_CRON=0 10 * * 1","INACTIVE_DAYS=90"],["Cron Trigger|Weekly scan","SQLite|Customer data","Code|Segmentation","IF|Value branch","Email|Offer sends","Spreadsheet|Campaign log"]),
# =========================== 51-65 CRM & Sales ===============================
(51,"HubSpot Lead Capture","CRM & Sales","Captures new HubSpot leads from web forms and enriches them.","HubSpot Trigger (Contact)","Fetch Lead Data","IF: Enrichment needed?","Enrich via API","Save Lead","Assign to Owner","Notify Sales Rep",
 [],["HUBSPOT_WEBHOOK_PATH=hubspot-lead"],["HubSpot Trigger|New contact","HTTP Request|Enrichment API","IF|Enrichment check","HubSpot|Create contact","HubSpot|Owner assignment","Slack|Sales alert"]),
(52,"Salesforce Lead Router","CRM & Sales","Routes Salesforce leads to the right sales owner by territory.","Salesforce Trigger (Lead)","Read Lead Territory","IF: APAC region?","Assign APAC Rep","Assign EMEA Rep","Update Lead Owner","Notify Assigned Rep",
 [],["SF_WEBHOOK_PATH=sf-lead-route"],["Salesforce Trigger|New lead","Code|Territory parse","IF|Region branch","Salesforce|Owner update","Salesforce|Lead update","Email|Rep notification"]),
(53,"Pipedrive Deal Sync","CRM & Sales","Syncs Pipedrive deals to a Google Sheets pipeline tracker.","Pipedrive Trigger (Deal)","Fetch Deal Fields","IF: Deal stage changed?","Update Sheet Row","Log Change","Notify Manager","Sync to Dashboard",
 [],["PIPEDRIVE_WEBHOOK_PATH=deal-sync"],["Pipedrive Trigger|Deal event","HTTP Request|Deal data","IF|Stage change","Google Sheets|Tracker update","Slack|Manager alert","Code|Dashboard sync"]),
(54,"Zoho CRM Enrichment","CRM & Sales","Enriches Zoho CRM records with company information automatically.","Zoho Trigger (Record)","Fetch Company Domain","IF: Data incomplete?","Enrich Company Info","Update Record","Log Enrichment","Notify Owner",
 [],["ZOHO_WEBHOOK_PATH=zoho-enrich"],["Zoho Trigger|Record event","HTTP Request|Company API","IF|Completeness check","Zoho|Update record","SQLite|Enrichment log","Email|Owner notify"]),
(55,"Lead Scoring Engine","CRM & Sales","Scores every inbound lead using behavior and profile signals.","Webhook (Lead)","Fetch Lead Signals","Compute Score","IF: Score over 80?","Mark as Hot Lead","Mark as Nurture","Update Score Field",
 [],["LEAD_WEBHOOK_PATH=score","HOT_SCORE=80"],["Webhook|Lead inbound","HTTP Request|Behavior data","Code|Score formula","IF|Hot threshold","CRM|Score field","Slack|Hot lead alert"]),
(56,"Lead Deduplication","CRM & Sales","Detects duplicate leads and merges them into a single record.","CRM Trigger (New Lead)","Lookup Existing Leads","IF: Match found?","Merge Records","Create New Lead","Log Dedupe","Notify Owner",
 ["n8n-nodes-sqlite"],["DEDUPE_WEBHOOK_PATH=dedupe"],["CRM Trigger|Lead create","SQLite|Lookup index","IF|Match detection","CRM|Merge action","CRM|Create record","SQLite|Dedupe log"]),
(57,"Lead Warm-up Sequence","CRM & Sales","Sends a multi-touch warm-up sequence to new leads.","CRM Trigger (Lead)","Start Sequence","Wait 2 Days","IF: Responded?","Stop Sequence","Send Email 3","Update Lead Stage",
 [],["WARMUP_STEPS=3","WARMUP_WAIT_DAYS=2"],["CRM Trigger|New lead","Email Send|First touch","Wait|Delay between","IF|Response check","Email Send|Follow-ups","CRM|Stage update"]),
(58,"Appointment Scheduler (Calendly)","CRM & Sales","Schedules appointments via Calendly and syncs to CRM.","Calendly Trigger (Booking)","Fetch Booking Details","IF: Slot confirmed?","Create CRM Task","Notify Booker","Add to Calendar","Send Confirmation",
 [],["CALENDLY_WEBHOOK_PATH=booking"],["Calendly Trigger|New booking","HTTP Request|Booking data","IF|Confirmation check","Google Calendar|Add event","CRM|Create task","Email|Confirmation"]),
(59,"Meeting Reminder","CRM & Sales","Sends meeting reminders to attendees before the start time.","Cron Trigger (Hourly)","Find Meetings in 1h","IF: Reminder sent?","Skip Meeting","Send Reminder Email","Notify Organizer","Log Reminders",
 [],["MEETING_CRON=0 * * * *","REMIND_BEFORE_MIN=60"],["Cron Trigger|Scan calendar","Google Calendar|Events","IF|Reminder check","Email|Reminder send","Slack|Organizer note","SQLite|Reminder log"]),
(60,"Post-Meeting Follow-up","CRM & Sales","Sends follow-up emails with notes and action items after meetings.","Calendar Trigger (Ended)","Fetch Meeting Notes","Build Follow-up Email","IF: Action items?","List Action Items","Send Summary Only","Update CRM Deal",
 [],["FOLLOWUP_WEBHOOK_PATH=meeting-followup"],["Calendar Trigger|Meeting end","Code|Notes parsing","IF|Action check","Email|Follow-up send","CRM|Deal update","Spreadsheet|Notes store"]),
(61,"CRM Task Auto-creator","CRM & Sales","Automatically creates follow-up tasks in CRM from email mentions.","Email Trigger (Mention)","Extract Actionable Text","IF: Action required?","Create CRM Task","Ignore Email","Assign Task Owner","Notify Assignee",
 [],["TASK_WEBHOOK_PATH=crm-task"],["Email Trigger|Inbound mail","AI|Action extraction","IF|Action detection","CRM|Create task","CRM|Assign owner","Slack|Assignee alert"]),
(62,"Sales Pipeline Dashboard","CRM & Sales","Keeps a live sales pipeline dashboard updated in Google Sheets.","Cron Trigger (15 min)","Fetch All Deals","IF: Stage changed?","Update Dashboard Row","Log Deal","Refresh Chart","Notify Sales Team",
 [],["PIPELINE_CRON=*/15 * * * *"],["Cron Trigger|Refresh","CRM API|Deal fetch","IF|Change detection","Google Sheets|Dashboard","Code|Chart data","Slack|Team update"]),
(63,"Monthly Sales Report","CRM & Sales","Generates and emails a monthly sales performance report.","Cron Trigger (Monthly)","Aggregate Sales Data","Compute KPIs","IF: Target met?","Mark Achievement","Show Gap","Email Report",
 [],["SALES_CRON=0 7 1 * *","TARGET_REVENUE=100000"],["Cron Trigger|Monthly run","SQLite|Sales data","Code|KPI compute","IF|Target check","Email|Report send","Google Sheets|Archive"]),
(64,"Quota vs Actual Tracker","CRM & Sales","Tracks sales rep quota attainment against actuals in real time.","Cron Trigger (Daily)","Fetch Rep Quotas","Fetch Actual Sales","IF: Below 80%?","Alert Rep + Manager","Log Progress","Update Scorecard",
 [],["QUOTA_CRON=0 8 * * *","QUOTA_WARN_PCT=80"],["Cron Trigger|Daily sync","CRM API|Quota data","CRM API|Actual sales","IF|Warning threshold","Email|Rep alert","Google Sheets|Scorecard"]),
(65,"Sales Lead Reassignment","CRM & Sales","Reassigns stale leads to a new owner automatically.","Cron Trigger (Weekly)","Find Stale Leads","IF: Stale > 14 days?","Reassign to Round-robin","Keep Lead","Notify New Owner","Log Reassignment",
 [],["REASSIGN_CRON=0 6 * * 1","STALE_DAYS=14"],["Cron Trigger|Weekly scan","CRM API|Lead age","IF|Stale threshold","CRM|Owner change","Email|New owner alert","SQLite|Reassign log"]),
# =========================== 66-75 Support & Customer Service ================
(66,"Zendesk Ticket Router","Support & Customer Service","Routes Zendesk tickets to teams by category and priority.","Zendesk Trigger (Ticket)","Classify Ticket Category","IF: Urgent priority?","Assign Urgent Queue","Assign Standard Queue","Set Ticket Fields","Notify Agent",
 ["n8n-nodes-discord"],["TICKET_WEBHOOK_PATH=ticket-route"],["Zendesk Trigger|New ticket","Code|Category detect","IF|Priority branch","Zendesk|Queue assign","Zendesk|Field update","Discord|Agent notify"]),
(67,"Freshdesk Ticket Auto-Reply","Support & Customer Service","Sends instant acknowledgements to Freshdesk tickets.","Freshdesk Trigger (Ticket)","Fetch Ticket Content","IF: Needs immediate reply?","Send Quick Answer","Send Ack Message","Add Internal Note","Log Auto-replies",
 [],["FRESHDESK_WEBHOOK_PATH=fd-ticket"],["Freshdesk Trigger|New ticket","Code|Content analysis","IF|Auto-reply check","Freshdesk|Reply post","Freshdesk|Internal note","SQLite|Reply log"]),
(68,"Jira Issue Creator","Support & Customer Service","Creates Jira issues automatically from support requests.","Email / Support Trigger","Parse Issue Details","IF: Duplicate issue?","Link Existing Issue","Create Jira Issue","Assign to Team","Notify Reporter",
 [],["JIRA_WEBHOOK_PATH=jira-create"],["Email Trigger|Support mail","Code|Issue parsing","IF|Duplicate check","Jira|Create issue","Jira|Assignment","Email|Reporter notify"]),
(69,"Slack Support Channel","Support & Customer Service","Posts new support tickets to a Slack channel for awareness.","Zendesk Trigger (Ticket)","Build Ticket Summary","Post to Support Channel","IF: VIP customer?","Mention Support Lead","Post Standard Alert","Log Posted Tickets",
 [],["SUPPORT_CHANNEL=support"],["Zendesk Trigger|Ticket event","Code|Summary build","Slack|Channel post","IF|VIP branch","Slack|Lead mention","SQLite|Post log"]),
(70,"FAQ Auto-Answerer","Support & Customer Service","Answers common support questions from a FAQ knowledge base.","Webhook (Question)","Match Question to FAQ","IF: Confidence high?","Send FAQ Answer","Route to Agent","Log Unanswered","Update FAQ Score",
 [],["FAQ_WEBHOOK_PATH=faq-answer","MIN_CONFIDENCE=0.8"],["Webhook|Question inbound","Code|FAQ matching","IF|Confidence check","Email/Chat|Answer send","Slack|Agent route","SQLite|Unanswered log"]),
(71,"Chat Transcript Analyzer","Support & Customer Service","Analyzes chat transcripts for quality and escalations.","Chat Trigger (Transcript)","Fetch Transcript","IF: Negative sentiment?","Flag for Review","Log Transcript","Score Quality","Email Summary",
 [],["CHAT_WEBHOOK_PATH=transcript"],["Chat Trigger|Transcript end","AI|Sentiment analysis","IF|Negative flag","Slack|Review flag","SQLite|Transcript store","Email|Quality report"]),
(72,"CSAT Survey Sender","Support & Customer Service","Sends customer satisfaction surveys after ticket resolution.","Ticket Trigger (Resolved)","Build CSAT Survey","IF: Eligible contact?","Send Survey Email","Skip Contact","Wait for Response","Store CSAT Score",
 [],["CSAT_WEBHOOK_PATH=csat","SURVEY_WAIT_DAYS=1"],["Ticket Trigger|Resolution","Code|Eligibility check","IF|Survey branch","Email|Survey send","Wait|Response window","Google Sheets|CSAT store"]),
(73,"Ticket Escalation Monitor","Support & Customer Service","Monitors SLA and escalates tickets that are about to breach.","Cron Trigger (30 min)","Check Ticket Ages","IF: Breach risk?","Escalate to Manager","Update SLA Status","Notify Support Lead","Log Escalations",
 [],["SLA_CRON=*/30 * * * *","SLA_HOURS=4"],["Cron Trigger|Age scan","Zendesk|Ticket fetch","IF|Breach risk","Email|Manager escalate","Zendesk|Status update","SQLite|Escalation log"]),
(74,"Support Handoff Notifier","Support & Customer Service","Notifies the right team when a ticket changes ownership.","Ticket Trigger (Assignee)","Fetch New Assignee","IF: Different team?","Notify New Team","Log Handoff","Add Handoff Note","Update Ticket History",
 [],["HANDOFF_WEBHOOK_PATH=handoff"],["Ticket Trigger|Assignee change","Code|Team detect","IF|Team change","Slack|Team notify","Zendesk|Internal note","SQLite|Handoff log"]),
(75,"Knowledge Base Updater","Support & Customer Service","Suggests knowledge base articles from resolved tickets.","Ticket Trigger (Resolved)","Extract Resolution Text","IF: Recurring issue?","Create KB Draft","Discard Suggestion","Send Draft for Review","Log KB Updates",
 ["n8n-nodes-baserow"],["KB_WEBHOOK_PATH=kb-draft","RECUR_COUNT=5"],["Ticket Trigger|Resolution","AI|Text extraction","IF|Recurrence check","Baserow|KB draft store","Email|Review request","SQLite|KB log"]),
# =========================== 76-90 Data & Database ===========================
(76,"Database Backup Scheduler","Data & Database","Schedules automatic backups of your databases to cloud storage.","Cron Trigger (Daily 2am)","Connect to Database","Create Dump","IF: Dump success?","Upload to S3","Retry Backup","Send Backup Report",
 ["n8n-nodes-mongodb","n8n-nodes-sqlite"],["BACKUP_CRON=0 2 * * *","BACKUP_DIR=/data"],["Cron Trigger|Backup schedule","Postgres|Database dump","Code|Dump create","IF|Success check","S3|Upload backup","Email|Backup report"]),
(77,"Database Health Monitor","Data & Database","Checks database health metrics and alerts on anomalies.","Cron Trigger (5 min)","Query Health Metrics","IF: Metric out of range?","Alert DBA","Log Healthy","Update Dashboard","Notify Team",
 [],["DB_HEALTH_CRON=*/5 * * * *","LATENCY_WARN_MS=500"],["Cron Trigger|Health poll","Postgres|Metrics query","IF|Threshold check","Slack|DBA alert","Google Sheets|Dashboard","SQLite|Health log"]),
(78,"SQL Query Reporter","Data & Database","Runs scheduled SQL queries and emails the results.","Cron Trigger (Daily)","Run SQL Query","Format Results","IF: Empty results?","Send Empty Notice","Email Full Report","Log Query Run",
 [],["SQL_REPORT_CRON=0 7 * * *","SQL_FILE=reports.sql"],["Cron Trigger|Daily run","Postgres|Query execute","Code|Format table","IF|Empty check","Email|Report send","SQLite|Run log"]),
(79,"CSV to Database Import","Data & Database","Imports CSV files into a database with validation.","File Trigger (CSV)","Parse CSV Rows","IF: Rows valid?","Insert into Database","Log Invalid Rows","Send Import Summary","Archive File",
 [],["CSV_IMPORT_WEBHOOK_PATH=csv-import"],["File Trigger|New CSV","Code|Row parsing","IF|Validation check","Postgres|Bulk insert","Google Sheets|Error log","Email|Import summary"]),
(80,"Database to CSV Export","Data & Database","Exports database tables to CSV and stores them on schedule.","Cron Trigger (Weekly)","Query Export Data","Build CSV File","IF: Data present?","Save to Drive","Log Empty Export","Email Download Link",
 [],["EXPORT_CRON=0 3 * * 1"],["Cron Trigger|Weekly export","Postgres|Query data","Code|CSV build","IF|Data check","Google Drive|Save file","Email|Link send"]),
(81,"Data Migration Assistant","Data & Database","Assists with migrating data between database systems.","Webhook (Migration)","Extract Source Data","Transform Schema","IF: Mapping complete?","Load into Target","Flag Missing Mappings","Log Migration",
 [],["MIGRATION_WEBHOOK_PATH=migrate"],["Webhook|Migration start","SQLite|Source extract","Code|Schema transform","IF|Mapping check","Postgres|Target load","Slack|DBA notify"]),
(82,"Data Deduplication Cleaner","Data & Database","Finds and removes duplicate records across datasets.","Cron Trigger (Monthly)","Scan for Duplicates","IF: Duplicate found?","Merge / Remove","Keep Record","Log Cleanup","Email Cleanup Report",
 [],["DEDUPE_CRON=0 4 1 * *"],["Cron Trigger|Monthly scan","Postgres|Scan query","IF|Duplicate detect","Postgres|Merge action","SQLite|Cleanup log","Email|Report send"]),
(83,"Data Validation Pipeline","Data & Database","Validates incoming data against business rules before storing.","Webhook (Data)","Apply Validation Rules","IF: Data valid?","Store in Database","Reject with Reason","Notify Data Owner","Log Validation",
 [],["VALIDATION_WEBHOOK_PATH=validate"],["Webhook|Data inbound","Code|Rule checks","IF|Valid branch","Postgres|Store record","Email|Rejection notice","SQLite|Validation log"]),
(84,"ETL Nightly Pipeline","Data & Database","Runs nightly extract-transform-load jobs between sources.","Cron Trigger (Nightly)","Extract from Sources","Transform Data","IF: Transforms pass?","Load to Warehouse","Retry Failed Steps","Send Pipeline Report",
 [],["ETL_CRON=0 1 * * *"],["Cron Trigger|Nightly job","HTTP Request|Extract","Code|Transform","IF|Pass check","Postgres|Load data","Email|Pipeline report"]),
(85,"MongoDB Collection Sync","Data & Database","Syncs collections between MongoDB databases.","Cron Trigger (Hourly)","Read Source Collection","IF: Documents changed?","Write to Target","Skip Unchanged","Log Sync","Alert on Errors",
 ["n8n-nodes-mongodb"],["MONGO_SYNC_CRON=0 * * * *","MONGO_SOURCE=mongodb://source"],["Cron Trigger|Hourly sync","MongoDB|Source read","IF|Change detection","MongoDB|Target write","SQLite|Sync log","Slack|Error alert"]),
(86,"PostgreSQL Change Tracker","Data & Database","Tracks changes to PostgreSQL tables and logs them.","Postgres Trigger (Change)","Capture Changed Rows","IF: Change type?","Log Insert / Update","Log Delete","Store Change Feed","Notify Subscribers",
 [],["PG_CHANGE_WEBHOOK_PATH=pg-change"],["Postgres Trigger|Table change","Postgres|Row capture","IF|Change type","SQLite|Change feed","Webhook|Subscriber push","Slack|Change alert"]),
(87,"MySQL Replication Monitor","Data & Database","Monitors MySQL replication lag and alerts on issues.","Cron Trigger (5 min)","Query Replication Status","IF: Lag > threshold?","Alert DBA","Log Status","Send Replication Report","Notify On-call",
 [],["MYSQL_LAG_CRON=*/5 * * * *","LAG_WARN_SECONDS=30"],["Cron Trigger|Lag poll","MySQL|Status query","IF|Lag check","Slack|DBA alert","SQLite|Status log","Email|Periodic report"]),
(88,"Excel Sheet Merger","Data & Database","Merges multiple Excel files into a single workbook.","File Trigger (Excel)","Read All Sheets","IF: Headers match?","Merge Rows","Flag Mismatch","Save Merged File","Notify Owner",
 [],["MERGE_WEBHOOK_PATH=merge-excel"],["File Trigger|New files","Spreadsheet File|Read sheets","Code|Header check","IF|Merge branch","Spreadsheet File|Save merged","Email|Owner notify"]),
(89,"Google Sheets Data Sync","Data & Database","Keeps Google Sheets in sync with a database.","Cron Trigger (Hourly)","Query Database","IF: Row changed?","Update Sheet Cell","Log Change","Add New Row","Notify Editor",
 [],["SHEET_SYNC_CRON=0 * * * *"],["Cron Trigger|Sync poll","Postgres|Query rows","IF|Change detect","Google Sheets|Cell update","Google Sheets|Append row","SQLite|Sync log"]),
(90,"File Format Converter","Data & Database","Converts files between formats (CSV, JSON, XML, Excel).","Webhook (File)","Detect Input Format","Transform to Target","IF: Conversion ok?","Save Converted File","Return Error","Log Conversion",
 [],["CONVERT_WEBHOOK_PATH=convert"],["Webhook|File upload","Code|Format detect","Code|Transform","IF|Success check","Google Drive|Save file","SQLite|Conversion log"]),
# =========================== 91-110 Developer & DevOps =======================
(91,"GitHub Issue Auto-labeler","Developer & DevOps","Auto-labels GitHub issues based on content.","GitHub Trigger (Issue)","Read Issue Title and Body","IF: Bug keywords?","Label as Bug","Label as Feature","Add Welcome Comment","Notify Assignee",
 ["n8n-nodes-github"],["GITHUB_WEBHOOK_PATH=issue-label","LABEL_RULES=bug,feature,docs"],["GitHub Trigger|Issue opened","Code|Keyword match","IF|Label branch","GitHub|Add label","GitHub|Comment post","Slack|Assignee notify"]),
(92,"GitHub PR Notifier","Developer & DevOps","Notifies the team when pull requests are created or updated.","GitHub Trigger (PR)","Fetch PR Details","IF: Draft or Ready?","Notify Draft Queue","Notify Review Queue","Post to Slack","Log PR Activity",
 ["n8n-nodes-github"],["PR_WEBHOOK_PATH=pr-event"],["GitHub Trigger|PR event","GitHub|PR details","IF|Draft check","Slack|Draft notify","Slack|Review notify","SQLite|PR log"]),
(93,"GitHub Release Tracker","Developer & DevOps","Watches GitHub releases and announces them.","GitHub Trigger (Release)","Fetch Release Notes","IF: Pre-release?","Skip Announce","Post Release Announcement","Send Changelog Digest","Log Releases",
 ["n8n-nodes-github","n8n-nodes-discord"],["RELEASE_WEBHOOK_PATH=release"],["GitHub Trigger|New release","GitHub|Release data","IF|Pre-release check","Discord|Announce post","Email|Changelog","SQLite|Release log"]),
(94,"GitLab Merge Request Bot","Developer & DevOps","Automates GitLab merge request notifications and approvals.","GitLab Trigger (MR)","Fetch MR Info","IF: Pipeline passing?","Request Approval","Flag Pipeline Failure","Post Comment","Notify Reviewers",
 [],["GITLAB_WEBHOOK_PATH=mr-event"],["GitLab Trigger|MR event","GitLab|MR details","IF|Pipeline check","GitLab|Approval request","GitLab|Comment post","Slack|Reviewer notify"]),
(95,"CI/CD Status Notifier","Developer & DevOps","Sends build status notifications after each pipeline run.","Webhook (Pipeline)","Fetch Build Status","IF: Build failed?","Alert Developers","Post Success","Log Builds","Notify Team Channel",
 [],["CI_WEBHOOK_PATH=ci-status"],["Webhook|Pipeline event","HTTP Request|Build API","IF|Failure check","Slack|Failure alert","Slack|Success post","SQLite|Build log"]),
(96,"Docker Event Watcher","Developer & DevOps","Monitors Docker events and logs container activity.","Webhook (Docker Event)","Parse Event Type","IF: Container stopped?","Alert On-call","Log Event","Update Status Board","Notify Team",
 [],["DOCKER_WEBHOOK_PATH=docker-event"],["Webhook|Docker event","Code|Event parsing","IF|Stop detection","Slack|On-call alert","SQLite|Event log","Google Sheets|Status board"]),
(97,"Kubernetes Alert Relay","Developer & DevOps","Relays Kubernetes cluster alerts to the operations team.","Webhook (K8s Alert)","Parse Alert Payload","IF: Critical severity?","Page On-call","Log Warning","Post to Ops Channel","Create Incident Ticket",
 [],["K8S_WEBHOOK_PATH=k8s-alert"],["Webhook|K8s alert","Code|Severity parse","IF|Critical branch","PagerDuty|Page on-call","Slack|Ops post","Jira|Incident ticket"]),
(98,"Log Aggregator","Developer & DevOps","Aggregates logs from multiple sources and indexes them.","Webhook (Logs)","Normalize Log Lines","IF: Error detected?","Flag for Search","Index Logs","Trigger Search Alert","Store in Database",
 ["n8n-nodes-mongodb"],["LOG_WEBHOOK_PATH=log-ingest"],["Webhook|Log ingest","Code|Normalization","IF|Error detect","MongoDB|Index logs","Slack|Error alert","Google Sheets|Log stats"]),
(99,"Error Tracker (Sentry)","Developer & DevOps","Sends Sentry error events to the development channel.","Sentry Trigger (Error)","Fetch Error Details","IF: New issue?","Create Slack Alert","Update Issue Count","Log Error","Notify Dev Lead",
 [],["SENTRY_WEBHOOK_PATH=sentry-event"],["Sentry Trigger|New error","HTTP Request|Error data","IF|New issue check","Slack|Dev alert","SQLite|Error log","Email|Dev lead note"]),
(100,"Website Uptime Monitor","Developer & DevOps","Checks website uptime and alerts when a site goes down.","Cron Trigger (5 min)","Ping Website","IF: HTTP 200?","Mark Online","Alert Down","Log Check","Notify On-call",
 [],["UPTIME_CRON=*/5 * * * *","TARGET_URL=https://example.com"],["Cron Trigger|Uptime poll","HTTP Request|Site ping","IF|Status check","Google Sheets|Online log","Slack|Down alert","Email|On-call notify"]),
(101,"SSL Certificate Expiry Alert","Developer & DevOps","Warns before SSL certificates expire.","Cron Trigger (Daily)","Check Cert Expiry","IF: < 14 days?","Send Expiry Alert","Log Cert Status","Update Cert Tracker","Notify Ops Team",
 [],["SSL_CRON=0 9 * * *","CERT_WARN_DAYS=14","DOMAIN_LIST=example.com"],["Cron Trigger|Daily check","Code|Cert fetch","IF|Expiry window","Email|Expiry alert","Google Sheets|Cert tracker","Slack|Ops notify"]),
(102,"Deploy Status Reporter","Developer & DevOps","Reports deployment status after each release.","Webhook (Deploy)","Fetch Deploy Result","IF: Deploy success?","Post Success Report","Post Failure Report","Update Status Page","Notify Stakeholders",
 [],["DEPLOY_WEBHOOK_PATH=deploy-status"],["Webhook|Deploy event","HTTP Request|Deploy API","IF|Result check","Slack|Success post","Slack|Failure post","Email|Stakeholder notify"]),
(103,"API Endpoint Monitor","Developer & DevOps","Monitors API endpoints for latency and availability.","Cron Trigger (1 min)","Hit API Endpoint","Measure Latency","IF: Slow or down?","Alert API Team","Store Metrics","Update Dashboard",
 [],["API_MONITOR_CRON=* * * * *","ENDPOINTS=health.json","LATENCY_WARN_MS=1000"],["Cron Trigger|Endpoint poll","HTTP Request|Request send","Code|Latency measure","IF|Threshold check","Slack|API alert","Google Sheets|Metrics"]),
(104,"Server Disk Space Alert","Developer & DevOps","Alerts when server disk space runs low.","Cron Trigger (Hourly)","Query Disk Usage","IF: Above 90%?","Alert Sysadmin","Log Usage","Send Weekly Report","Clean Temp Files",
 [],["DISK_CRON=0 * * * *","DISK_WARN_PCT=90"],["Cron Trigger|Usage poll","HTTP Request|Metrics API","IF|Threshold check","Slack|Sysadmin alert","SQLite|Usage log","Email|Weekly report"]),
(105,"Rate Limit Guardian","Developer & DevOps","Monitors API rate limits and queues requests to avoid 429s.","Webhook (Request)","Check Remaining Quota","IF: Quota low?","Queue Request","Send Request","Log Throttles","Alert API Owner",
 [],["QUOTA_WEBHOOK_PATH=throttle","QUOTA_WARN_PCT=20"],["Webhook|Request inbound","HTTP Request|Quota check","IF|Quota branch","SQLite|Queue store","HTTP Request|Send","Slack|Owner alert"]),
(106,"Webhook Debugger","Developer & DevOps","Receives webhook payloads and lets developers inspect them.","Webhook (Payload)","Pretty-print Payload","IF: Fields valid?","Show to Developer","Flag Malformed","Store Payload","Notify Developer",
 [],["DEBUG_WEBHOOK_PATH=debug"],["Webhook|Payload inbound","Code|Pretty print","IF|Validation check","Slack|Dev notification","MongoDB|Payload store","Email|Malformed alert"]),
(107,"API Documentation Generator","Developer & DevOps","Generates API documentation from request logs.","Cron Trigger (Weekly)","Fetch Request Logs","Build Documentation","IF: New endpoints?","Add to Docs","Skip Endpoints","Publish Docs",
 [],["DOCS_CRON=0 5 * * 1"],["Cron Trigger|Weekly run","SQLite|Request logs","Code|Docs build","IF|New endpoint","Google Docs|Publish","Slack|API team notify"]),
(108,"Microservice Health Check","Developer & DevOps","Checks the health of all microservices in a stack.","Cron Trigger (5 min)","Poll All Services","IF: Any unhealthy?","Alert On-call","Log All Healthy","Send Status Snapshot","Notify Team",
 [],["MS_HEALTH_CRON=*/5 * * * *","SERVICE_LIST=service-a,service-b"],["Cron Trigger|Health poll","HTTP Request|Service check","IF|Health branch","Slack|On-call alert","Google Sheets|Status board","SQLite|Health log"]),
(109,"Cron Job Validator","Developer & DevOps","Validates cron schedules and reports upcoming runs.","Cron Trigger (Daily)","Parse Cron Expressions","IF: Expression valid?","Log Schedule","Flag Invalid","Send Schedule Report","Notify Admins",
 [],["CRON_VALIDATOR=0 6 * * *"],["Cron Trigger|Daily check","Code|Expression parse","IF|Validation branch","Google Sheets|Schedule log","Email|Report send","Slack|Admin notify"]),
(110,"Code Coverage Reporter","Developer & DevOps","Collects code coverage results and posts them after CI runs.","Webhook (Coverage)","Parse Coverage Report","IF: Coverage dropped?","Alert Dev Team","Post Coverage Summary","Update Tracker","Notify Maintainers",
 [],["COVERAGE_WEBHOOK_PATH=coverage"],["Webhook|Coverage event","Code|Parse report","IF|Drop detection","Slack|Dev alert","GitHub|PR comment","Google Sheets|Coverage tracker"]),
# =========================== 111-125 AI & LLM ================================
(111,"AI Chat Assistant","AI & LLM","Builds an AI chatbot that answers questions from your data.","Webhook (User Chat)","Load Context Documents","IF: Retrieval ok?","Answer with RAG","Fallback Answer","Stream Response","Log Conversation",
 ["n8n-nodes-mcp"],["CHAT_WEBHOOK_PATH=chat","LLM_MODEL=your-model"],["Webhook|User message","Vector Store|Context load","AI Agent|RAG answer","IF|Retrieval check","Webhook|Response send","SQLite|Conversation log"]),
(112,"AI Content Writer","AI & LLM","Generates blog and social content from a topic list.","Spreadsheet Trigger (Topics)","Build Prompt","IF: Style selected?","Generate Article","Generate Short Post","Save Content","Notify Editor",
 ["n8n-nodes-mcp"],["CONTENT_WEBHOOK_PATH=content-gen"],["Spreadsheet File|Topic list","AI LLM|Content generate","IF|Style branch","Google Docs|Save article","Google Sheets|Save posts","Slack|Editor notify"]),
(113,"AI Summarizer","AI & LLM","Summarizes long documents and emails automatically.","Webhook (Document)","Extract Text","IF: Length over limit?","Summarize Chunks","Summarize Full Text","Return Summary","Log Usage",
 [],["SUMMARIZE_WEBHOOK_PATH=summary","CHUNK_SIZE=4000"],["Webhook|Document in","Code|Text extract","IF|Length check","AI LLM|Chunk summary","AI LLM|Full summary","SQLite|Usage log"]),
(114,"AI Sentiment Analyzer","AI & LLM","Analyzes sentiment of reviews and messages at scale.","Webhook (Text)","Classify Sentiment","IF: Negative score?","Alert Support","Tag Positive / Neutral","Store Score","Update Dashboard",
 [],["SENTIMENT_WEBHOOK_PATH=sentiment"],["Webhook|Text inbound","AI LLM|Sentiment score","IF|Negative branch","Slack|Support alert","Google Sheets|Score store","SQLite|Analysis log"]),
(115,"AI Lead Enrichment","AI & LLM","Enriches leads with AI-generated company summaries.","CRM Trigger (Lead)","Fetch Company Data","IF: Existing summary?","Skip Enrichment","Generate AI Summary","Update Lead Field","Notify Sales",
 [],["AI_ENRICH_WEBHOOK_PATH=enrich"],["CRM Trigger|New lead","HTTP Request|Company data","IF|Dup check","AI LLM|Summary generate","CRM|Field update","Slack|Sales notify"]),
(116,"AI Translation Service","AI & LLM","Translates content between languages automatically.","Webhook (Translate)","Detect Language","IF: Target set?","Translate Text","Use Default Target","Return Translation","Log Requests",
 [],["TRANSLATE_WEBHOOK_PATH=translate"],["Webhook|Text inbound","Code|Language detect","IF|Target check","AI LLM|Translate","Webhook|Response send","SQLite|Request log"]),
(117,"AI Document Classifier","AI & LLM","Classifies uploaded documents into categories.","Webhook (Document)","Extract Document Text","IF: Confidence high?","Assign Category","Flag for Review","Update Record","Notify Owner",
 [],["CLASSIFY_WEBHOOK_PATH=classify"],["Webhook|File upload","Code|Text extract","AI LLM|Category classify","IF|Confidence check","Google Sheets|Category store","Slack|Review flag"]),
(118,"AI Email Drafter","AI & LLM","Drafts email responses for support agents to review.","Email Trigger (Support)","Summarize Thread","Generate Draft Reply","IF: Approved?","Send Draft","Save for Edit","Log Drafts",
 [],["DRAFT_WEBHOOK_PATH=email-draft"],["Email Trigger|Inbound thread","AI LLM|Draft generate","IF|Approval branch","Email Send|Send reply","Google Docs|Draft store","SQLite|Draft log"]),
(119,"AI Support Bot (RAG)","AI & LLM","Answers support questions using retrieval-augmented generation over your docs.","Webhook (Support Chat)","Search Knowledge Base","IF: Answer found?","Reply with Sources","Request Clarification","Log Sessions","Improve KB",
 ["n8n-nodes-mcp"],["RAG_WEBHOOK_PATH=support-bot"],["Webhook|Chat message","Vector Store|KB search","AI Agent|Answer build","IF|Confidence check","Webhook|Reply send","SQLite|Session log"]),
(120,"AI Meeting Note Taker","AI & LLM","Transcribes meetings and extracts action items.","Calendar Trigger (Meeting)","Fetch Recording / Transcript","IF: Transcript exists?","Extract Action Items","Request Transcript","Send Summary Email","Archive Notes",
 [],["NOTES_WEBHOOK_PATH=meeting-notes"],["Calendar Trigger|Meeting end","HTTP Request|Transcript","AI LLM|Action extract","IF|Transcript check","Email|Summary send","Google Docs|Notes archive"]),
(121,"AI Image Generator","AI & LLM","Generates images from text prompts for content creation.","Webhook (Prompt)","Build Image Prompt","IF: Style specified?","Generate Artwork","Use Default Style","Save Image","Notify Creator",
 ["n8n-nodes-mcp"],["IMAGE_WEBHOOK_PATH=image-gen"],["Webhook|Prompt inbound","AI LLM|Prompt build","IF|Style branch","HTTP Request|Image API","Google Drive|Save image","Slack|Creator notify"]),
(122,"AI Text-to-Speech Notifier","AI & LLM","Converts text alerts into audio notifications.","Webhook (Alert)","Build Speech Text","IF: Urgent alert?","Generate Audio","Send Text Alert","Send Audio File","Log Notifications",
 [],["TTS_WEBHOOK_PATH=tts-alert"],["Webhook|Alert event","Code|Text build","IF|Urgency check","HTTP Request|TTS API","Telegram|Audio send","SQLite|Notification log"]),
(123,"AI Data Extractor","AI & LLM","Extracts structured data from unstructured documents.","Webhook (Document)","Send Document to AI","IF: Fields extracted?","Map to Database","Flag Extraction Error","Store Data","Notify User",
 [],["EXTRACT_WEBHOOK_PATH=ai-extract"],["Webhook|Document in","AI LLM|Field extract","IF|Success check","Postgres|Store data","Slack|Error flag","Email|User notify"]),
(124,"AI Workflow Optimizer","AI & LLM","Analyzes workflow logs and suggests optimizations.","Cron Trigger (Weekly)","Fetch Execution Logs","IF: Bottleneck found?","Suggest Optimization","Log Healthy","Send AI Report","Archive Analysis",
 [],["OPTIMIZE_CRON=0 6 * * 1"],["Cron Trigger|Weekly run","SQLite|Execution logs","AI LLM|Analyze logs","IF|Bottleneck check","Email|AI report","Google Sheets|Analysis store"]),
(125,"AI Code Reviewer","AI & LLM","Reviews pull requests and posts AI code feedback.","GitHub Trigger (PR)","Fetch PR Diff","IF: Changed files?","Generate Review","Post Review Comment","Log Review","Notify Author",
 ["n8n-nodes-github","n8n-nodes-mcp"],["AI_REVIEW_WEBHOOK_PATH=code-review"],["GitHub Trigger|PR open","GitHub|Diff fetch","AI LLM|Review generate","IF|Diff check","GitHub|Comment post","SQLite|Review log"]),
# =========================== 126-140 Finance & Accounting ====================
(126,"Invoice Generator","Finance & Accounting","Generates invoices from order data and emails them.","Order Webhook","Build Invoice Data","IF: Tax applicable?","Add Tax Line","Generate Invoice PDF","Email Invoice","Log Invoice",
 ["n8n-nodes-mongodb"],["INVOICE_WEBHOOK_PATH=invoice","TAX_RATE=0.0"],["Webhook|Order event","Code|Invoice build","IF|Tax check","PDF|Generate document","Email|Send invoice","MongoDB|Invoice archive"]),
(127,"Payment Reminder Bot","Finance & Accounting","Reminds customers about overdue payments.","Cron Trigger (Daily)","Find Overdue Invoices","IF: Overdue days > 7?","Send Strong Reminder","Send Soft Reminder","Update Reminder Log","Notify Finance",
 ["n8n-nodes-stripe","n8n-nodes-sqlite"],["REMIND_CRON=0 9 * * *","REMINDER_LEVELS=soft,strong"],["Cron Trigger|Daily scan","SQLite|Invoice store","IF|Overdue level","Email|Reminder send","Stripe|Payment check","Google Sheets|Reminder log"]),
(128,"Expense Tracker","Finance & Accounting","Tracks expenses from receipts and categorizes them.","Email Trigger (Receipt)","Extract Receipt Data","IF: Amount valid?","Categorize Expense","Flag Receipt","Append to Ledger","Notify Approver",
 [],["EXPENSE_WEBHOOK_PATH=expense"],["Email Trigger|Receipt mail","AI LLM|Receipt parse","IF|Amount check","Google Sheets|Ledger append","Slack|Approver notify","SQLite|Expense log"]),
(129,"Payroll Summary Reporter","Finance & Accounting","Compiles payroll summaries for the finance team.","Cron Trigger (Monthly)","Fetch Timesheets","Compute Totals","IF: Discrepancy found?","Flag for Review","Generate Summary","Email Report",
 [],["PAYROLL_CRON=0 6 1 * *"],["Cron Trigger|Monthly run","Google Sheets|Timesheets","Code|Total compute","IF|Discrepancy check","Google Sheets|Summary","Email|Report send"]),
(130,"Tax Document Collector","Finance & Accounting","Collects and organizes tax documents before deadlines.","Cron Trigger (Quarterly)","Request Missing Docs","IF: All received?","Sort by Category","Send Reminders","Store Documents","Notify Accountant",
 [],["TAX_CRON=0 8 1 * *"],["Cron Trigger|Quarterly run","Email|Doc requests","IF|Completeness check","Google Drive|Sort files","Email|Reminder send","Slack|Accountant notify"]),
(131,"Bank Transaction Categorizer","Finance & Accounting","Categorizes bank transactions for bookkeeping.","Cron Trigger (Daily)","Fetch Transactions","IF: Pattern known?","Auto-categorize","Flag for Review","Update Ledger","Send Daily Summary",
 [],["BANK_CRON=0 5 * * *"],["Cron Trigger|Daily fetch","HTTP Request|Bank API","Code|Pattern match","IF|Category match","Google Sheets|Ledger","Email|Daily summary"]),
(132,"Subscription Cost Analyzer","Finance & Accounting","Analyzes SaaS subscription costs across the company.","Cron Trigger (Monthly)","Collect Subscription Bills","IF: Cost over budget?","Alert Finance","Log Costs","Generate Report","Notify Stakeholders",
 [],["SUB_CRON=0 7 1 * *","SUB_BUDGET=5000"],["Cron Trigger|Monthly run","HTTP Request|Billing APIs","IF|Budget check","Slack|Finance alert","Google Sheets|Cost log","Email|Report send"]),
(133,"Currency Exchange Alert","Finance & Accounting","Alerts when currency exchange rates hit targets.","Cron Trigger (Hourly)","Fetch Exchange Rates","IF: Rate target hit?","Send Rate Alert","Log Rates","Update Tracker","Notify Trader",
 [],["FX_CRON=0 * * * *","FX_TARGET=1.10"],["Cron Trigger|Rate poll","HTTP Request|FX API","IF|Target check","Email|Rate alert","Google Sheets|Rate tracker","Slack|Trader notify"]),
(134,"Stock Price Monitor","Finance & Accounting","Monitors stock prices and sends alerts on movements.","Cron Trigger (15 min)","Fetch Stock Quotes","IF: Price limit hit?","Send Price Alert","Log Prices","Update Watchlist","Notify Investor",
 [],["STOCK_CRON=*/15 * * * *","STOCK_SYMBOL=APPL"],["Cron Trigger|Quote poll","HTTP Request|Stock API","IF|Limit check","Email|Price alert","Google Sheets|Watchlist","SQLite|Price log"]),
(135,"Crypto Portfolio Tracker","Finance & Accounting","Tracks crypto portfolio value and daily changes.","Cron Trigger (Hourly)","Fetch Coin Prices","Compute Portfolio Value","IF: Change > 5%?","Send Change Alert","Update Tracker","Log Snapshot",
 [],["CRYPTO_CRON=0 * * * *","COINS=BTC,ETH","ALERT_PCT=5"],["Cron Trigger|Price poll","HTTP Request|Coin API","Code|Value compute","IF|Change threshold","Google Sheets|Portfolio tracker","Email|Change alert"]),
(136,"Crypto Price Alert","Finance & Accounting","Sends alerts when crypto prices cross thresholds.","Cron Trigger (5 min)","Fetch Coin Price","IF: Above / below?","Send Buy / Sell Alert","Log Price","Update Alerts Board","Notify Trader",
 [],["CRYPTO_ALERT_CRON=*/5 * * * *","PRICE_HIGH=60000"],["Cron Trigger|Price poll","HTTP Request|Coin API","IF|Threshold check","Telegram|Alert send","Google Sheets|Alerts board","SQLite|Price log"]),
(137,"Invoice Matching","Finance & Accounting","Matches invoices against purchase orders automatically.","Webhook (Invoice)","Fetch Purchase Order","IF: Amount matches?","Approve for Payment","Flag Mismatch","Log Matching","Notify AP Team",
 [],["MATCH_WEBHOOK_PATH=invoice-match"],["Webhook|Invoice in","HTTP Request|PO lookup","IF|Amount check","Google Sheets|Approval log","Slack|AP alert","SQLite|Match log"]),
(138,"Revenue Reconciler","Finance & Accounting","Reconciles revenue between payment processors and books.","Cron Trigger (Daily)","Fetch Payment Totals","Fetch Book Totals","IF: Difference?","Create Adjustments","Mark Reconciled","Email Reconciliation Report",
 ["n8n-nodes-stripe"],["RECON_CRON=0 4 * * *"],["Cron Trigger|Daily reconcile","Stripe|Payment totals","HTTP Request|Book totals","IF|Diff check","Google Sheets|Adjustments","Email|Report send"]),
(139,"Budget Alert System","Finance & Accounting","Alerts department heads when budgets approach limits.","Cron Trigger (Weekly)","Fetch Department Spend","IF: Over 80% budget?","Alert Department Head","Log Spending","Update Budget Dashboard","Send Weekly Summary",
 [],["BUDGET_CRON=0 9 * * 1","BUDGET_WARN_PCT=80"],["Cron Trigger|Weekly check","SQLite|Spend data","IF|Threshold check","Email|Head alert","Google Sheets|Budget dashboard","Slack|Finance notify"]),
(140,"Financial KPI Dashboard","Finance & Accounting","Updates a financial KPI dashboard from multiple sources.","Cron Trigger (Daily)","Collect Financial KPIs","IF: KPI missing?","Flag Missing Data","Compute Metrics","Update Dashboard","Email KPI Summary",
 [],["KPI_CRON=0 6 * * *"],["Cron Trigger|Daily run","SQLite|KPI data","Code|Metric compute","IF|Missing check","Google Sheets|Dashboard","Email|KPI summary"]),
# =========================== 141-155 HR & Internal Ops =======================
(141,"New Hire Onboarding","HR & Internal Ops","Automates the new hire onboarding checklist and welcome emails.","HR Trigger (Hire)","Create Onboarding Tasks","IF: Role has equipment?","Order Equipment","Send Welcome Email","Grant Access","Notify Manager",
 [],["ONBOARD_WEBHOOK_PATH=onboard"],["HR Trigger|New hire","Google Sheets|Task list","IF|Equipment check","Email|Access requests","Email|Welcome send","Slack|Manager notify"]),
(142,"Employee Welcome Kit","HR & Internal Ops","Sends a digital welcome kit to new employees.","HR Trigger (Hire)","Build Welcome Kit","IF: PDF version?","Send PDF Kit","Send Online Kit","Add to Wiki","Notify Buddy",
 [],["WELCOME_WEBHOOK_PATH=welcome-kit"],["HR Trigger|New hire","Code|Kit build","IF|Format branch","Email|Kit send","Google Drive|Wiki add","Slack|Buddy notify"]),
(143,"Leave Request Approver","HR & Internal Ops","Routes leave requests to managers for approval.","HR Trigger (Leave Request)","Fetch Request Details","IF: Available balance?","Notify Manager","Reject Request","Update Leave Calendar","Log Decision",
 [],["LEAVE_WEBHOOK_PATH=leave"],["HR Trigger|Leave request","Code|Balance check","IF|Balance branch","Email|Manager approval","Google Calendar|Leave update","SQLite|Decision log"]),
(144,"Timesheet Validator","HR & Internal Ops","Validates submitted timesheets and flags issues.","HR Trigger (Timesheet)","Check Hours Entries","IF: Over 40 hours?","Flag Overtime","Validate Entries","Update Payroll Sheet","Notify Employee",
 [],["TIMESHEET_WEBHOOK_PATH=timesheet"],["HR Trigger|Timesheet submit","Code|Hours check","IF|Overtime flag","Google Sheets|Payroll update","Email|Employee notify","SQLite|Validation log"]),
(145,"Expense Approval Workflow","HR & Internal Ops","Routes expense claims through an approval chain.","HR Trigger (Expense)","Validate Receipt","IF: Under 100?","Auto-approve","Forward to Manager","Update Ledger","Notify Employee",
 [],["EXPENSE_APPROVE_WEBHOOK_PATH=expense-approve","AUTO_APPROVE_LIMIT=100"],["HR Trigger|Expense claim","Code|Receipt check","IF|Amount branch","Email|Approval request","Google Sheets|Ledger","Slack|Employee notify"]),
(146,"Interview Scheduler","HR & Internal Ops","Coordinates interview slots between candidates and panels.","Webhook (Interview)","Fetch Candidate Availability","IF: Panel free?","Book Interview","Suggest Alternatives","Send Invite","Log Scheduling",
 ["n8n-nodes-zoom"],["INTERVIEW_WEBHOOK_PATH=interview"],["Webhook|Interview request","Google Calendar|Availability","IF|Slot check","Zoom|Create meeting","Email|Invite send","Google Sheets|Schedule log"]),
(147,"Candidate Screening","HR & Internal Ops","Screens job applicants by matching skills to requirements.","HR Trigger (Application)","Parse Candidate Resume","IF: Skills match?","Move to Shortlist","Send Rejection","Update Pipeline","Notify Recruiter",
 [],["SCREEN_WEBHOOK_PATH=screen"],["HR Trigger|Application","AI LLM|Resume parse","IF|Match check","Google Sheets|Pipeline update","Email|Rejection send","Slack|Recruiter notify"]),
(148,"Reference Check Requester","HR & Internal Ops","Requests and tracks reference checks for final candidates.","HR Trigger (Candidate)","Fetch Reference Contacts","Send Reference Form","IF: All received?","Update Candidate Record","Send Reminder","Notify HR",
 [],["REFERENCE_WEBHOOK_PATH=reference"],["HR Trigger|Final candidate","Email|Form send","Wait|Response window","IF|Completeness check","Google Sheets|Candidate record","Slack|HR notify"]),
(149,"HR Newsletter Sender","HR & Internal Ops","Sends company newsletters to employees on a schedule.","Cron Trigger (Monthly)","Build Newsletter Content","IF: Attachments ready?","Send with Attachments","Send Text Only","Update Send Log","Track Engagement",
 [],["HR_NEWS_CRON=0 10 1 * *"],["Cron Trigger|Monthly send","Google Docs|Content build","IF|Attachment check","Email|Newsletter send","Spreadsheet|Send log","SQLite|Engagement log"]),
(150,"Employee Anniversary Greeting","HR & Internal Ops","Automatically greets employees on work anniversaries.","Cron Trigger (Daily)","Check Anniversary Dates","IF: Anniversary today?","Send Greeting","Skip Day","Post to Team Channel","Log Greetings",
 [],["ANNIVERSARY_CRON=0 9 * * *"],["Cron Trigger|Daily check","SQLite|Employee records","IF|Date match","Email|Greeting send","Slack|Team channel post","SQLite|Greeting log"]),
(151,"Equipment Request Tracker","HR & Internal Ops","Tracks hardware and equipment requests from intake to delivery.","Webhook (Equipment Request)","Log Request Details","IF: Stock available?","Create Dispatch Task","Add to Waitlist","Notify Requester","Update Inventory",
 [],["EQUIPMENT_WEBHOOK_PATH=equipment"],["Webhook|Request in","Google Sheets|Request log","IF|Stock check","Slack|Dispatch task","Email|Requester notify","SQLite|Inventory update"]),
(152,"Offboarding Checklist","HR & Internal Ops","Runs the offboarding checklist when employees leave.","HR Trigger (Offboarding)","Create Checklist","IF: Has company assets?","Collect Assets","Revoke Access","Send Exit Survey","Notify IT",
 [],["OFFBOARD_WEBHOOK_PATH=offboard"],["HR Trigger|Departure","Google Sheets|Checklist","IF|Asset check","Email|Asset return","IT|Access revoke","Email|Exit survey"]),
(153,"Training Course Enroller","HR & Internal Ops","Enrolls employees in required training courses automatically.","HR Trigger (Role Change)","Match Course to Role","IF: Course exists?","Enroll Employee","Flag Missing Course","Send Course Invite","Update Training Log",
 [],["TRAINING_WEBHOOK_PATH=training"],["HR Trigger|Role change","Code|Course match","IF|Course check","Email|Invite send","Google Sheets|Training log","Slack|HR notify"]),
(154,"Team Event Planner","HR & Internal Ops","Coordinates team events, polls and logistics.","Webhook (Event Idea)","Create Event Draft","IF: Date confirmed?","Send Invites","Poll for Availability","Book Venue / Lunch","Update Calendar",
 [],["EVENT_WEBHOOK_PATH=team-event"],["Webhook|Event idea","Google Calendar|Date check","IF|Confirmation branch","Email|Invite send","Poll API|Availability","Google Sheets|Event plan"]),
(155,"Travel Request Processor","HR & Internal Ops","Processes travel requests and books approved trips.","HR Trigger (Travel)","Validate Policy","IF: Approved?","Book Flight / Hotel","Send Policy Feedback","Update Travel Log","Notify Traveler",
 [],["TRAVEL_WEBHOOK_PATH=travel"],["HR Trigger|Travel request","Code|Policy check","IF|Approval branch","HTTP Request|Booking API","Email|Itinerary send","Google Sheets|Travel log"]),
# =========================== 156-170 Content & Publishing =====================
(156,"Blog Post Scheduler","Content & Publishing","Schedules and publishes blog posts across platforms.","Google Sheets Trigger (Posts)","Fetch Post Content","IF: Date reached?","Publish to CMS","Queue for Later","Notify Editor","Update Status",
 [],["BLOG_CRON=0 11 * * *"],["Google Sheets|Post queue","Code|Date check","IF|Publish branch","HTTP Request|CMS API","Email|Editor notify","Spreadsheet|Status update"]),
(157,"Medium Article Republisher","Content & Publishing","Republishes blog posts to Medium automatically.","RSS Trigger (New Post)","Fetch Article HTML","IF: Images included?","Upload with Images","Publish Text","Update Canonical Link","Log Republish",
 [],["MEDIUM_WEBHOOK_PATH=medium-pub"],["RSS Trigger|New post","HTTP Request|Article fetch","IF|Image check","Medium API|Publish","Code|Canonical link","SQLite|Republish log"]),
(158,"Podcast Episode Notifier","Content & Publishing","Notifies listeners when new podcast episodes go live.","RSS Trigger (Episode)","Fetch Episode Metadata","IF: Published today?","Post to Socials","Queue in Newsletter","Notify Audience","Log Episodes",
 ["n8n-nodes-telegram","n8n-nodes-discord"],["PODCAST_RSS=feed-url"],["RSS Trigger|New episode","Code|Metadata extract","IF|Date check","Twitter|Social post","Telegram|Audience notify","SQLite|Episode log"]),
(159,"SEO Keyword Tracker","Content & Publishing","Tracks keyword rankings and reports movements.","Cron Trigger (Weekly)","Fetch Rankings","IF: Rank improved?","Mark Green","Mark Red","Update Tracker","Email SEO Report",
 [],["SEO_CRON=0 8 * * 1"],["Cron Trigger|Weekly run","HTTP Request|Rank API","IF|Change check","Google Sheets|Rank tracker","Email|SEO report","Slack|SEO team notify"]),
(160,"Content Idea Collector","Content & Publishing","Collects content ideas from multiple sources into one board.","Webhook (Idea)","Normalize Idea","IF: Duplicate?","Skip Idea","Add to Ideas Board","Tag by Topic","Notify Editor",
 [],["IDEA_WEBHOOK_PATH=idea"],["Webhook|Idea inbound","Code|Normalize","IF|Dup check","Baserow|Ideas board","Code|Topic tags","Slack|Editor notify"]),
(161,"Brand Kit Consistency Check","Content & Publishing","Checks content against brand guidelines.","Webhook (Content)","Extract Colors and Fonts","IF: Matches brand?","Approve Content","Flag Violation","Log Checks","Notify Brand Manager",
 [],["BRAND_CHECK_WEBHOOK_PATH=brand-check"],["Webhook|Content submit","Code|Brand extract","IF|Match check","Google Sheets|Approval log","Slack|Brand manager alert","SQLite|Check log"]),
(162,"Press Release Distributor","Content & Publishing","Distributes press releases to media contacts.","Webhook (Press Release)","Load Contact List","IF: Has release PDF?","Send with PDF","Send Text Version","Track Opens","Notify PR Team",
 [],["PRESS_WEBHOOK_PATH=press-release"],["Webhook|Release ready","Google Sheets|Media list","IF|Attachment check","Email|Send release","Email|Open tracking","Slack|PR team notify"]),
(163,"E-book Lead Magnet Sender","Content & Publishing","Sends e-books to leads who opt in via a form.","Webhook (Opt-in)","Add to List","IF: Verified email?","Send E-book Link","Flag Invalid","Log Downloads","Notify Marketing",
 [],["EBOOK_WEBHOOK_PATH=ebook"],["Webhook|Opt-in form","Code|Email verify","IF|Verification branch","Email|E-book send","Google Sheets|Download log","Slack|Marketing notify"]),
(164,"Webinar Registration Funnel","Content & Publishing","Manages webinar registration and reminders.","Webhook (Registration)","Add to Webinar List","Send Confirmation","IF: Day before event?","Send Reminder","Wait for Event","Send Follow-up",
 ["n8n-nodes-zoom"],["WEBINAR_WEBHOOK_PATH=webinar","REMINDER_CRON=0 9 * * *"],["Webhook|Registration","Email|Confirmation","Cron Trigger|Reminder","Zoom|Meeting link","Email|Follow-up","Google Sheets|Attendance"]),
(165,"Event RSVP Tracker","Content & Publishing","Tracks RSVPs and sends event updates.","Webhook (RSVP)","Update RSVP Count","IF: Capacity reached?","Notify Organizer","Send Confirmation","Add to Guest List","Send Day-of Reminder",
 [],["RSVP_WEBHOOK_PATH=rsvp","MAX_CAPACITY=100"],["Webhook|RSVP event","Google Sheets|Guest list","IF|Capacity check","Email|Confirmation","Slack|Organizer alert","Email|Reminder send"]),
(166,"YouTube to Blog Converter","Content & Publishing","Turns YouTube videos into blog post drafts.","YouTube Trigger (Video)","Fetch Transcript","IF: Transcript length ok?","Generate Blog Draft","Skip Video","Save Draft","Notify Editor",
 ["n8n-nodes-mcp"],["YT_TO_BLOG_WEBHOOK_PATH=yt-blog"],["YouTube Trigger|New video","HTTP Request|Transcript","AI LLM|Draft generate","IF|Length check","Google Docs|Save draft","Slack|Editor notify"]),
(167,"Quote Generator for Blog","Content & Publishing","Adds relevant quotes to blog posts automatically.","Webhook (Post)","Extract Post Topic","IF: Quote available?","Insert Quote","Leave Placeholder","Update Post","Log Quotations",
 [],["QUOTE_WEBHOOK_PATH=quote"],["Webhook|Post content","Code|Topic extract","IF|Quote match","Code|Quote insert","Google Docs|Post update","SQLite|Quote log"]),
(168,"Plagiarism Checker","Content & Publishing","Checks blog content for plagiarism before publishing.","Webhook (Content)","Send to Checker","IF: Similarity high?","Flag for Rewrite","Approve Content","Log Checks","Notify Editor",
 [],["PLAGIARISM_WEBHOOK_PATH=plagiarism"],["Webhook|Content submit","HTTP Request|Plagiarism API","IF|Similarity check","Google Docs|Flag copy","Slack|Editor notify","SQLite|Check log"]),
(169,"Content Calendar Syncer","Content & Publishing","Syncs content calendars between teams and tools.","Cron Trigger (Daily)","Fetch Calendar Events","IF: Date changed?","Update All Calendars","Log Changes","Notify Team","Send Daily Digest",
 [],["CALENDAR_SYNC_CRON=0 6 * * *"],["Cron Trigger|Daily sync","Google Calendar|Events","IF|Change detection","Google Sheets|Calendar store","Slack|Team notify","Email|Digest send"]),
(170,"Backlink Monitor","Content & Publishing","Monitors new backlinks to your content.","Cron Trigger (Weekly)","Fetch Backlink Data","IF: New backlink?","Add to Tracker","Skip Duplicate","Rate Link Quality","Notify SEO Team",
 [],["BACKLINK_CRON=0 7 * * 1"],["Cron Trigger|Weekly scan","HTTP Request|Backlink API","IF|New link check","Google Sheets|Backlink tracker","Code|Quality score","Slack|SEO team notify"]),
# =========================== 171-180 IoT & Smart Home ========================
(171,"Weather Alert System","IoT & Smart Home","Sends weather alerts based on live conditions and thresholds.","Cron Trigger (30 min)","Fetch Weather Data","IF: Severe condition?","Send Alert","Log Conditions","Update Weather Board","Notify Subscribers",
 ["n8n-nodes-openweathermap","n8n-nodes-telegram"],["WEATHER_CRON=*/30 * * * *","CITY=London"],["Cron Trigger|Weather poll","OpenWeatherMap|Weather fetch","IF|Severity check","Telegram|Alert send","SQLite|Weather log","Google Sheets|Weather board"]),
(172,"Smart Home Notifier","IoT & Smart Home","Sends notifications for smart home device events.","Webhook (Device Event)","Parse Event","IF: Security event?","Send Security Alert","Log Routine Event","Update Device State","Notify Owner",
 [],["SMART_HOME_WEBHOOK_PATH=device-event"],["Webhook|Device event","Code|Event parse","IF|Security check","Telegram|Security alert","SQLite|State store","Email|Owner notify"]),
(173,"Air Quality Monitor","IoT & Smart Home","Monitors air quality and alerts on pollution spikes.","Cron Trigger (Hourly)","Fetch Air Quality","IF: AQI over 100?","Send Health Alert","Log AQI","Update Dashboard","Notify Subscribers",
 [],["AQI_CRON=0 * * * *","AQI_WARN=100"],["Cron Trigger|AQI poll","HTTP Request|AQI API","IF|Threshold check","Telegram|Health alert","SQLite|AQI log","Google Sheets|Dashboard"]),
(174,"Fitness Streak Reminder","IoT & Smart Home","Tracks fitness streaks and sends motivation reminders.","Cron Trigger (Daily)","Check Activity Log","IF: Streak broken?","Send Reboot Message","Send Streak Update","Update Tracker","Notify User",
 [],["FITNESS_CRON=0 8 * * *"],["Cron Trigger|Daily check","HTTP Request|Activity API","IF|Streak check","Telegram|Motivation","Google Sheets|Tracker","Email|Daily update"]),
(175,"Plant Watering Reminder","IoT & Smart Home","Sends reminders when plants need water based on sensor data.","Cron Trigger (Daily)","Read Moisture Sensors","IF: Soil dry?","Send Watering Reminder","Log Moisture","Update Plant Status","Notify Owner",
 [],["PLANT_CRON=0 9 * * *","MOISTURE_WARN=30"],["Cron Trigger|Daily read","HTTP Request|Sensor API","IF|Dry check","Telegram|Reminder send","SQLite|Moisture log","Google Sheets|Plant status"]),
(176,"IoT Sensor Data Logger","IoT & Smart Home","Logs sensor data from IoT devices into a database.","Webhook (Sensor)","Normalize Reading","IF: Reading valid?","Store in Database","Flag Anomaly","Update Dashboard","Alert on Extreme",
 ["n8n-nodes-mongodb"],["SENSOR_WEBHOOK_PATH=sensor"],["Webhook|Sensor reading","Code|Normalize","IF|Valid check","MongoDB|Store reading","Google Sheets|Dashboard","Slack|Extreme alert"]),
(177,"Traffic Alert System","IoT & Smart Home","Sends traffic alerts before the daily commute.","Cron Trigger (Daily)","Fetch Traffic Data","IF: Congestion high?","Send Route Alert","Log Traffic","Suggest Alternative","Notify Commuter",
 [],["TRAFFIC_CRON=0 7 * * 1-5","CONGESTION_WARN=70"],["Cron Trigger|Morning check","HTTP Request|Traffic API","IF|Congestion check","Telegram|Route alert","SQLite|Traffic log","Email|Alternatives send"]),
(178,"Earthquake Alert Forwarder","IoT & Smart Home","Forwards earthquake alerts to affected regions.","Webhook (Seismic Event)","Fetch Event Details","IF: Magnitude over 5?","Send Critical Alert","Log Event","Update Map","Notify Authorities",
 [],["EARTHQUAKE_WEBHOOK_PATH=seismic"],["Webhook|Seismic event","HTTP Request|Event data","IF|Magnitude check","Telegram|Critical alert","Google Sheets|Event map","Email|Authorities notify"]),
(179,"Sunrise / Sunset Scheduler","IoT & Smart Home","Triggers actions based on sunrise and sunset times.","Cron Trigger (Daily)","Fetch Sun Times","IF: After sunrise?","Run Day Actions","Run Night Actions","Log Runs","Notify Owner",
 [],["SUN_CRON=0 5 * * *"],["Cron Trigger|Sun check","HTTP Request|Sun API","IF|Time branch","HTTP Request|Device action","SQLite|Run log","Telegram|Owner notify"]),
(180,"Energy Usage Tracker","IoT & Smart Home","Tracks home energy usage and sends weekly reports.","Cron Trigger (Hourly)","Read Energy Meter","IF: Usage spike?","Send Spike Alert","Store Reading","Compute Weekly Use","Email Weekly Report",
 [],["ENERGY_CRON=0 * * * *","SPIKE_WATT=3000"],["Cron Trigger|Meter read","HTTP Request|Energy API","IF|Spike check","SQLite|Usage store","Code|Weekly compute","Email|Report send"]),
# =========================== 181-190 Monitoring & Alerts =====================
(181,"Server Incident Responder","Monitoring & Alerts","Responds to server incidents with automated runbooks.","Alert Webhook","Classify Incident","IF: Known issue?","Run Fix Runbook","Create Incident Ticket","Notify On-call","Log Resolution",
 [],["INCIDENT_WEBHOOK_PATH=incident"],["Webhook|Alert inbound","AI|Incident classify","IF|Known issue","Code|Runbook run","Jira|Ticket create","Slack|On-call alert"]),
(182,"Error Rate Threshold Alert","Monitoring & Alerts","Alerts when application error rates cross thresholds.","Cron Trigger (5 min)","Fetch Error Metrics","IF: Rate over 2%?","Send Alert","Log Metrics","Update Dashboard","Escalate if Persistent",
 [],["ERROR_ALERT_CRON=*/5 * * * *","ERROR_RATE_WARN=2"],["Cron Trigger|Metrics poll","HTTP Request|APM API","IF|Threshold check","Slack|Alert send","Google Sheets|Dashboard","Email|Escalation"]),
(183,"Business Hours Tracker","Monitoring & Alerts","Tracks service availability during business hours.","Cron Trigger (5 min)","Check Service Status","IF: Within business hours?","Log Availability","Skip Check","Compute Uptime","Email Weekly Uptime",
 [],["AVAIL_CRON=*/5 * * * *","BIZ_HOURS=9-17"],["Cron Trigger|Status poll","HTTP Request|Service check","IF|Hours window","SQLite|Availability log","Code|Uptime compute","Email|Uptime report"]),
(184,"Task Deadline Reminder","Monitoring & Alerts","Reminds teams about upcoming task deadlines.","Cron Trigger (Daily)","Fetch Due Tasks","IF: Due within 24h?","Send Reminder","Log Deadlines","Escalate if Late","Notify Task Owner",
 [],["DEADLINE_CRON=0 8 * * *","REMIND_WINDOW_H=24"],["Cron Trigger|Deadline scan","SQLite|Task store","IF|Window check","Email|Reminder send","Slack|Escalation","Google Sheets|Deadline log"]),
(185,"Daily Standup Summary","Monitoring & Alerts","Collects standup updates and posts a team summary.","Cron Trigger (Daily)","Collect Updates","Compile Summary","IF: Blockers reported?","Flag Blockers","Post Summary","Archive Updates",
 [],["STANDUP_SUMMARY_CRON=0 18 * * *"],["Cron Trigger|End of day","Slack|Update collect","Code|Summary build","IF|Blocker check","Slack|Summary post","Google Sheets|Archive"]),
(186,"Weekly Report Generator","Monitoring & Alerts","Generates weekly activity reports for stakeholders.","Cron Trigger (Weekly)","Collect Metrics","Build Report","IF: Data complete?","Send Report","Flag Missing Data","Archive Report",
 [],["WEEKLY_REPORT_CRON=0 16 * * 5"],["Cron Trigger|Weekly run","SQLite|Metric store","Code|Report build","IF|Completeness check","Email|Report send","Google Sheets|Archive"]),
(187,"Monthly KPI Digest","Monitoring & Alerts","Sends a monthly KPI digest to leadership.","Cron Trigger (Monthly)","Compute Monthly KPIs","Build Digest","IF: KPI vs target?","Add Variance Note","Standard Format","Email Digest",
 [],["KPI_DIGEST_CRON=0 9 1 * *"],["Cron Trigger|Monthly run","SQLite|KPI data","Code|Variance compute","IF|Target check","Email|Digest send","Google Sheets|KPI log"]),
(188,"Performance Alert Digest","Monitoring & Alerts","Sends a digest of all performance alerts from the day.","Cron Trigger (Daily)","Collect Day's Alerts","IF: Alerts found?","Email Alert Digest","Send No-alert Note","Summarize Severity","Archive Digest",
 [],["PERF_DIGEST_CRON=0 20 * * *"],["Cron Trigger|End of day","SQLite|Alert store","IF|Alert check","Email|Digest send","Code|Severity summary","Google Sheets|Archive"]),
(189,"Security Breach Notifier","Monitoring & Alerts","Notifies on security events from monitoring tools.","Security Webhook","Classify Event","IF: Critical severity?","Page Security Team","Log Event","Create Investigation Ticket","Notify Executives",
 [],["SECURITY_WEBHOOK_PATH=security"],["Webhook|Security event","Code|Severity classify","IF|Critical check","PagerDuty|Page team","Jira|Investigation ticket","Email|Exec notify"]),
(190,"Phishing Report Monitor","Monitoring & Alerts","Monitors user-reported phishing emails.","Email Trigger (Report)","Fetch Reported Email","IF: Confirmed phishing?","Block Sender","Add to Watchlist","Log Report","Notify Security Team",
 [],["PHISHING_WEBHOOK_PATH=phishing"],["Email Trigger|User report","Code|Analyze email","IF|Confirmed check","Email|Block action","SQLite|Watchlist","Slack|Security notify"]),
# =========================== 191-200 API Integration & Automation ============
(191,"Webhook Aggregation Gateway","API Integration & Automation","Aggregates multiple webhooks into one endpoint.","Webhook (Multiple)","Normalize Payloads","IF: Source known?","Route to Handler","Log Unknown","Store Event","Notify Subscribers",
 [],["GATEWAY_WEBHOOK_PATH=gateway"],["Webhook|Event inbound","Code|Payload normalize","IF|Source match","Webhook|Route forward","SQLite|Event store","Slack|Unknown alert"]),
(192,"Multi-API Enrichment","API Integration & Automation","Enriches records using multiple external APIs.","CRM Trigger (Record)","Fetch Base Record","IF: Data missing?","Call Enrichment APIs","Keep Record","Merge Results","Update Record",
 [],["ENRICHMENT_WEBHOOK_PATH=enrichment"],["CRM Trigger|Record event","HTTP Request|Enrich APIs","IF|Missing check","Code|Result merge","CRM|Record update","SQLite|Enrichment log"]),
(193,"OAuth Token Refresher","API Integration & Automation","Refreshes OAuth tokens before they expire.","Cron Trigger (Hourly)","Check Token Expiry","IF: Expires in 1h?","Refresh Token","Store New Token","Alert on Failure","Notify Integration Owner",
 [],["OAUTH_CRON=0 * * * *","REFRESH_WINDOW_MIN=60"],["Cron Trigger|Token check","SQLite|Token store","IF|Expiry window","HTTP Request|Refresh call","SQLite|Token update","Slack|Failure alert"]),
(194,"API Rate Limiter Queue","API Integration & Automation","Queues API calls to respect rate limits.","Webhook (Request)","Check Current Usage","IF: Limit reached?","Queue Request","Send Request","Replay Queue","Log Throttling",
 [],["RATE_QUEUE_WEBHOOK_PATH=rate-queue"],["Webhook|Request inbound","HTTP Request|Usage check","IF|Limit check","SQLite|Queue store","HTTP Request|Send","Google Sheets|Throttle log"]),
(195,"Webhook Retry Handler","API Integration & Automation","Retries failed webhook deliveries with backoff.","Webhook (Delivery)","Check Delivery Status","IF: Failed?","Retry with Backoff","Mark Delivered","Log Attempts","Alert After Max",
 [],["RETRY_WEBHOOK_PATH=retry","MAX_RETRIES=5"],["Webhook|Delivery event","Code|Status check","IF|Failure branch","Wait|Backoff delay","HTTP Request|Retry send","SQLite|Attempt log"]),
(196,"Public REST API Wrapper","API Integration & Automation","Wraps a public REST API behind a normalized endpoint.","Webhook (Request)","Map Request Params","IF: Auth required?","Fetch Token","Call External API","Transform Response","Return JSON",
 [],["REST_WRAPPER_WEBHOOK_PATH=api"],["Webhook|Client request","Code|Param mapping","IF|Auth check","HTTP Request|API call","Code|Response transform","Webhook|JSON return"]),
(197,"GraphQL Query Runner","API Integration & Automation","Runs GraphQL queries and posts results.","Webhook (Query)","Validate Query","IF: Query allowed?","Execute GraphQL","Reject Query","Format Results","Notify Consumer",
 [],["GRAPHQL_WEBHOOK_PATH=graphql"],["Webhook|Query inbound","Code|Validation","IF|Allow check","HTTP Request|GraphQL call","Code|Result format","SQLite|Query log"]),
(198,"WebSocket Event Listener","API Integration & Automation","Listens to WebSocket events and processes them.","WebSocket Trigger (Event)","Parse Event Message","IF: Event type known?","Process Event","Log Unknown Type","Store Event","Notify Subscribers",
 [],["WS_WEBHOOK_PATH=websocket"],["WebSocket Trigger|Event stream","Code|Message parse","IF|Type check","HTTP Request|Process","SQLite|Event store","Slack|Unknown alert"]),
(199,"iPaaS Style Data Router","API Integration & Automation","Routes data between systems like an integration platform.","Webhook (Record)","Detect Target System","IF: Mapping exists?","Transform and Send","Flag Missing Mapping","Log Route","Notify Integration Team",
 [],["ROUTER_WEBHOOK_PATH=router"],["Webhook|Record inbound","Code|Target detect","IF|Mapping check","HTTP Request|Send target","Google Sheets|Missing log","Slack|Integration alert"]),
(200,"Data Warehouse Syncer","API Integration & Automation","Syncs data from sources into a data warehouse.","Cron Trigger (Hourly)","Pull Source Data","IF: Schema changed?","Update Schema","Sync Data","Log Sync State","Alert on Failure",
 ["n8n-nodes-baserow"],["DW_SYNC_CRON=0 * * * *"],["Cron Trigger|Sync schedule","HTTP Request|Source pull","IF|Schema check","Postgres|Load data","Baserow|Warehouse tables","Slack|Failure alert"]),
]
# fmt: on

VERIFIED_COMMUNITY = [
    "n8n-nodes-telegram",
    "n8n-nodes-mcp",
    "n8n-nodes-mongodb",
    "n8n-nodes-sqlite",
    "n8n-nodes-discord",
    "n8n-nodes-github",
    "n8n-nodes-stripe",
    "n8n-nodes-baserow",
    "n8n-nodes-zoom",
    "n8n-nodes-openweathermap",
]

CATEGORIES = [
    "Email & Communication",
    "Social Media & Marketing",
    "E-commerce & Retail",
    "CRM & Sales",
    "Support & Customer Service",
    "Data & Database",
    "Developer & DevOps",
    "AI & LLM",
    "Finance & Accounting",
    "HR & Internal Ops",
    "Content & Publishing",
    "IoT & Smart Home",
    "Monitoring & Alerts",
    "API Integration & Automation",
]


def slugify(title):
    s = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    return s


def clean_label(text):
    return text.replace('"', "").replace("\n", " ")


def dockerfile(num, title, community, env_kvs):
    lines = []
    lines.append("# =============================================================================")
    lines.append(f"# Use Case {num:03d} - {title}")
    lines.append("# -----------------------------------------------------------------------------")
    lines.append("# n8n self-hosted Docker image for: {0}.".format(title))
    lines.append("# Built on the official n8n community image. Runs locally on Docker Desktop.")
    lines.append("#")
    lines.append("# Build:")
    lines.append(f"#   docker build -t n8n-usecase-{num:03d} .")
    lines.append("# Run:")
    lines.append("#   docker run -d --name n8n-usecase-{0:03d} -p 5678:5678 \\".format(num))
    lines.append("#     -v ~/.n8n:/home/node/.n8n n8n-usecase-{0:03d}".format(num))
    lines.append("# =============================================================================")
    lines.append("FROM n8nio/n8n:latest")
    lines.append("")
    lines.append("USER root")
    lines.append("")
    if community:
        lines.append("# Install verified community nodes from npm registry:")
        lines.append("RUN cd /usr/local/lib/node_modules/n8n \\")
        lines.append("    && npm install {0} --save \\".format(" ".join(community)))
        lines.append("    && npm cache clean --force")
    else:
        lines.append("# This use case is powered by n8n built-in nodes (400+ included).")
        lines.append("# Add community nodes later if needed, e.g.:")
        lines.append("# RUN cd /usr/local/lib/node_modules/n8n \\")
        lines.append("#     && npm install n8n-nodes-mcp --save \\")
        lines.append("#     && npm cache clean --force")
    lines.append("")
    lines.append("# Use-case specific environment defaults (override at runtime with -e):")
    env_entries = [
        "N8N_PROTOCOL=http",
        "N8N_HOST=localhost",
        "TZ=UTC",
        f"N8N_ENCRYPTION_KEY=CHANGE_ME_{num:03d}_STRONG_KEY",
    ] + list(env_kvs)
    lines.append("ENV " + " \\\n    ".join(env_entries))
    lines.append("")
    lines.append("EXPOSE 5678")
    lines.append('VOLUME ["/home/node/.n8n"]')
    lines.append("")
    lines.append("USER node")
    lines.append('ENTRYPOINT ["docker-entrypoint.sh"]')
    return "\n".join(lines) + "\n"


def diagram(num, u):
    _, title, _, _, trigger, step1, step2, condition, action_yes, action_no, output, _, _, _ = u
    # Normalize so the "IF:" condition always sits at the branch node (D).
    if step2.startswith("IF:") and not condition.startswith("IF:"):
        step2, condition = condition, step2
    t = clean_label(trigger)
    s1 = clean_label(step1)
    s2 = clean_label(step2)
    c = clean_label(condition)
    ay = clean_label(action_yes)
    an = clean_label(action_no)
    o = clean_label(output)
    return (
        "```mermaid\n"
        "flowchart TD\n"
        f'    A["{t}"]\n'
        f'    B["{s1}"]\n'
        f'    C["{s2}"]\n'
        f'    D["{c}"]\n'
        f'    E["{ay}"]\n'
        f'    F["{an}"]\n'
        f'    G["{o}"]\n'
        "    A --> B --> C --> D\n"
        '    D -- "Yes" --> E --> G\n'
        '    D -- "No" --> F --> G\n'
        "```\n"
    )


def readme(num, u, comm):
    n, title, category, desc, trigger, step1, step2, condition, action_yes, action_no, output, community, env_kvs, nodes = u
    d = dockerfile(num, title, community, env_kvs)
    diag = diagram(num, u)
    slug = slugify(title)
    folder = f"{num:02d}-{slug}"

    node_rows = "\n".join(
        f"| {row.split('|')[0].strip()} | {row.split('|')[1].strip()} |" for row in nodes
    )

    comm_txt = ", ".join(f"`{c}`" for c in community) if community else "None (built-in nodes)"
    env_txt = "".join(f"- `{kv}`\n" for kv in env_kvs)

    body = f"""# {num:03d} - {title}

> **Category:** {category}

{desc} Runs fully on your local machine via Docker Desktop - lifetime free.

## Architecture Diagram

{diag}
## Key Nodes

| Node | Purpose |
|------|---------|
{node_rows}

## Dockerfile

Dockerfile: [usecases/{folder}/Dockerfile](https://github.com/rahuleraser/AI_Agent_LLM_011_n8n/blob/main/usecases/{folder}/Dockerfile)

| Detail | Value |
|--------|-------|
| Base image | `n8nio/n8n:latest` |
| Community nodes | {comm_txt} |
| Exposed port | 5678 |
| Persistence | `~/.n8n` volume |

### Environment defaults

{env_txt}
## Build & Run

```bash
cd usecases/{folder}

# Build the image
docker build -t n8n-usecase-{num:03d} .

# Run on Docker Desktop
docker run -d --name n8n-usecase-{num:03d} -p 5678:5678 \\
  -v ~/.n8n:/home/node/.n8n n8n-usecase-{num:03d}

# Open http://localhost:5678
```

## Docker Compose (optional)

```yaml
services:
  n8n-usecase-{num:03d}:
    image: n8n-usecase-{num:03d}
    container_name: n8n-usecase-{num:03d}
    restart: unless-stopped
    ports: ["5678:5678"]
    volumes: ["n8n_usecase_{num:03d}_data:/home/node/.n8n"]

volumes:
  n8n_usecase_{num:03d}_data:
```

## Cost

$0 - no n8n license, no cloud hosting. Uses your local resources only. Any third-party API you connect (e.g. Gmail, Slack) uses its own free tier.
"""
    return body


def generate():
    os.makedirs(UC_ROOT, exist_ok=True)
    rows = []
    for u in UC:
        num, title, category, desc, trigger, step1, step2, condition, action_yes, action_no, output, community, env_kvs, nodes = u
        slug = slugify(title)
        folder = os.path.join(UC_ROOT, f"{num:02d}-{slug}")
        os.makedirs(folder, exist_ok=True)

        with open(os.path.join(folder, "Dockerfile"), "w") as f:
            f.write(dockerfile(num, title, community, env_kvs))
        with open(os.path.join(folder, "README.md"), "w") as f:
            f.write(readme(num, u, community))

        docker_url = f"{REPO}/blob/main/usecases/{num:02d}-{slug}/Dockerfile"
        diagram_url = f"{REPO}/blob/main/usecases/{num:02d}-{slug}/README.md"
        rows.append(
            f"| {num:02d} | {title} | {category} | [Dockerfile]({docker_url}) | [Diagram]({diagram_url}) |"
        )
        print(f"generated {num:02d}-{slug}")

    # main README table fragment
    table = "\n".join(rows)
    with open(os.path.join(ROOT, "usecases", "_INDEX.md"), "w") as f:
        f.write(table + "\n")
    print(f"\nTotal use cases generated: {len(UC)}")


if __name__ == "__main__":
    generate()
