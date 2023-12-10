# FixTwitterEmbed

A bot that makes your twitter links better

https://github.com/LTurret/FixTwitterEmbed/assets/22392956/40215909-fd3e-453a-a8a2-838df3894920

## Requirements

```plaintext
aiohttp==3.8.6
aiosignal==1.3.1
async-timeout==4.0.3
attrs==23.1.0
charset-normalizer==3.3.1
discord-py-interactions==5.10.0
discord-typings==0.7.0
emoji==2.8.0
frozenlist==1.4.0
idna==3.4
multidict==6.0.4
python-dotenv==1.0.0
tomli==2.0.1
typing_extensions==4.8.0
yarl==1.9.2
```

## Running

### Local

```shell
python3 -B main.py
```

### pm2

```shell
pm2 start main.py --name "arisa" --interpreter "python3" --interpreter-args "-B"
```

## License

Licensed under [MIT](LICENSE).
