# Commands Structure Pattern

## Directory Organization

This directory follows a clean, modular pattern for organizing CLI commands:

### Pattern Rules

1. **Each command group gets its own directory**
   ```
   commands/subs/
     s3/          # S3 commands
     onnx/        # ONNX commands
     build/       # Build commands (if complex)
   ```

2. **Directory structure for command groups**
   ```
   s3/
     __init__.py      # Router only - imports and registers subcommands
     upload.py        # Individual command implementation
     download.py      # Individual command implementation
     list.py          # Individual command implementation
     configure.py     # Individual command implementation
     bucket.py        # Subgroup with its own commands
     acl.py           # Subgroup with its own commands
     utils.py         # Shared utilities for this command group
   ```

3. **Router pattern (__init__.py)**
   - Contains only the Click group definition
   - Imports all subcommands
   - Registers them with `.add_command()`
   - NO implementation logic

   ```python
   """S3 command router - imports all subcommands"""

   import click

   from commands.subs.s3.upload import upload
   from commands.subs.s3.download import download
   # ... other imports

   @click.group()
   def s3() -> None:
       """S3 artifact management"""
       pass

   # Add all subcommands
   s3.add_command(upload)
   s3.add_command(download)
   # ... other commands
   ```

4. **Simple commands stay as single files**
   - If a command is simple (< 100 lines), keep it as a single file
   - Examples: `clean.py`, `dev.py`

5. **Import in main.py**
   ```python
   from commands.subs.s3 import s3  # Import from directory
   from commands.subs.build import build  # Import from directory
   ```

### Benefits

1. **Small files** - Each command in its own file (< 500 lines rule)
2. **Clear organization** - Easy to find commands
3. **Modular** - Easy to add/remove commands
4. **Shared utilities** - Each command group can have its own utils
5. **Scalable** - Pattern works for any number of commands

### Migration Guide

When a single-file command grows too large:

1. Create a directory with the command name
2. Create `__init__.py` with the router pattern
3. Move each subcommand to its own file
4. Move shared functions to `utils.py`
5. Update imports in `main.py`

### Example: S3 Command Structure

```
s3/
  __init__.py      # Router: @click.group() def s3()
  upload.py        # @click.command() def upload()
  download.py      # @click.command() def download()
  list.py          # @click.command(name="list") def list_artifacts()
  configure.py     # @click.command() def configure()
  bucket.py        # @click.group() def bucket() with subcommands
  acl.py           # @click.group() def acl() with subcommands
  utils.py         # get_aws_cmd() and other shared functions
```

### Example: Mirror Command Structure (Nested Groups)

For commands with multiple subgroups, create nested directories:

```
mirror/
  __init__.py      # Main router: @click.group() def mirror()
  onnx/
    __init__.py    # Subgroup router: @click.group() def onnx()
    push.py        # @click.command() def push()
    pull.py        # @click.command() def pull()
  pcaudio/
    __init__.py    # Subgroup router: @click.group() def pcaudio()
    push.py        # @click.command() def push()
    pull.py        # @click.command() def pull()
  ort/
    __init__.py    # Subgroup router: @click.group() def ort()
    fetch.py       # @click.command() def fetch()
```

This pattern:
- Keeps related commands together
- Makes it easy to find specific functionality
- Allows for shared utilities within each subgroup
- Scales well as more commands are added

This keeps each file focused and under 500 lines while maintaining a clean, predictable structure.

## Mirror Commands Pattern

The mirror commands follow a specific pattern for S3 and CloudFront usage:

### Key Principle: Push to S3, Pull from CloudFront

1. **Push commands** (`cli mirror * push`)
   - Upload artifacts directly to S3
   - Use AWS credentials for authentication
   - S3 paths configured in: `config/project-config.json`
   - Also update catalog.json with metadata

2. **Pull commands** (`cli mirror * pull`)
   - Download from CloudFront for speed and reliability
   - CloudFront URL and paths from: `config/project-config.json`
   - Falls back to S3 if CloudFront unavailable

3. **Vendor commands** (`cli vendor *`)
   - Download from external sites (GitHub, HuggingFace, etc.)
   - Cache locally for reuse
   - These are the original sources

### Example Flow

```bash
# 1. First time: fetch from external vendor
cli vendor onnx libs fetch --target darwin --arch arm64

# 2. Push to S3 for team/CI access
cli mirror onnx push --target darwin --arch arm64

# 3. Future builds: pull from CloudFront (fast)
cli mirror onnx pull --target darwin --arch arm64
```

### Configuration

All S3 bucket, CloudFront URLs, and path prefixes are defined in:
- `config/project-config.json` - See the `s3` section

This pattern ensures:
- Fast downloads via CloudFront CDN
- Reliable uploads to S3
- Clear separation between external vendors and our mirror