# Deploy to Streamlit Cloud

## Quick Deploy

1. **Push to GitHub**
```bash
git add .
git commit -m "Deploy CV screening dashboard"
git push origin main
```

2. **Deploy on Streamlit Cloud**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Click "New app"
   - Select your repo → Branch: `main` → Main file: `dashboard.py`
   - Click "Deploy"

3. **Done!** App will be live in 3-5 minutes.

## Troubleshooting

**CVs not showing?** Check CV folder path in sidebar matches `./junior fullstack developer`

**results.csv not found?** Verify file is in root directory and committed to Git

**PDF rendering fails?** Ensure `packages.txt` is committed

## Security

⚠️ Make GitHub repo **private** - CVs contain personal data
