# limehome-devops-challenge

## Coding Challenge

:warning: The author of this script assumes, that you already have python3 installed in your system, as well as aws-cli, and your AWS credentials and configs are already configured.

The script has 2 mandatory arguments to be defined when running, and 1 optional argument.

    **-b** - specify S3 bucket name, where the search is needed
    **-s** - specify the substring you would like to search.
    *-p*   - specify AWS profile to use for the session if it differs from "default"

Python `--help` snippet
```
usage: demo.py [-h] -b S3_BUCKET_NAME -s SUBSTRING [-p PROFILE]
  -b S3_BUCKET_NAME  S3 bucket name
  -s SUBSTRING       substring to find
  -p PROFILE         AWS profile to use
```

### How to run
```
python3 demo.py -b << YOUR S3 BUCKET NAME>> -s << SUBSTRING>> -p(can be omitted) << PROFILE NAME>>
```

---

## Devops Challenge Concepts

Could be found in `Devops Challenge Concepts Answers.txt`.

I tried to provide as much comprehensive answers as possible based both on my own experience and the Internet articles, and to do it in a very high-level terms.
