# Development Guide

This guide provides step-by-step instructions for setting up and running the AI Governance Framework website locally.

## Prerequisites

- Ruby (version 2.7 or higher)
- Git

## Initial Setup

### 1. Install Jekyll and Bundler

```bash
gem install jekyll bundler
```

### 2. Clone the Project

```bash
git clone https://github.com/finos/ai-governance-framework.git
cd ai-governance-framework
```

### 3. Choose Your Setup Method

#### Option A: Simple Setup (Recommended)
If you have Jekyll installed globally, you can run commands directly:

```bash
cd docs
jekyll serve
```

#### Option B: Bundle Setup (Isolated Dependencies)
For a more isolated environment or if you encounter dependency conflicts:

```bash
cd docs
bundle init
bundle add jekyll
bundle add webrick
bundle install
```

## Running the Site Locally

Navigate to the `docs/` directory:

```bash
cd docs
```

### Common Jekyll Commands

#### Simple Setup (Option A):
- Clean the build: `jekyll clean`
- Build the site: `jekyll build`  
- Serve locally: `jekyll serve`

#### Bundle Setup (Option B):
- Clean the build: `bundle exec jekyll clean`
- Build the site: `bundle exec jekyll build`  
- Serve locally: `bundle exec jekyll serve`

### Development Server

After running `jekyll serve` (or `bundle exec jekyll serve`), access the local development server at:
`http://localhost:4000`

The server will automatically reload when changes are made to the source files.

## Troubleshooting

- Ensure you're in the `docs/` directory when running Jekyll commands
- If you encounter dependency issues, try running `bundle install` again
- For permission issues with gem installation, consider using a Ruby version manager like rbenv or RVM

## Contributing

Once you have the site running locally, you can:
- Make changes to content files in `_risks/` and `_mitigations/`
- Preview your changes in real-time
- Test the site before submitting pull requests

For more details on content conventions, see [CONVENTIONS.md](CONVENTIONS.md).

For more details on how to contribute, see [CONTRIBUTING.md](CONTRIBUTING.md).