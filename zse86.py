#!/usr/bin/env python
# _*_coding:utf-8_*_

import execjs

paramsJoin = '3_2.0+/api/v4/search/suggest?q=%E7%9F%A5%E4%B9%8E+https://www.zhihu.com/search?type=content&q=%E7%9F%A5%E4%B9%8E+"AKCbAYqKoRGPTndjq59vw_0zYboL1wKawBk=|1595678620"+3_2.0ae3TnRUTEvOOUCNMTQnTSHUZo02p-HNMZBO8YDQqcXtubT2qB6P0E6rq-LS9-hp1DufI-we8gGHPgJO1xuPZ0GxCTJHR7820XM20cLRGDJXfgGCBxupMuD_Ie8FL7AtqM6O1VDQyQ6nxrRPCHukMoCXBEgOsiRP0XL2ZUBXmDDV9qhnyTXFMnXcTF_ntRueThiOM0crqEcSfIUe90Uo8qUCGPvLmSCXMjULqAgpCygHYD93MHGCOVhUBrwYPv0N8ubL0JcUOFCC_awXGvCcLJQX1UBp9-De019XyBCeLnwLVIwCO5hSVgwH09h3MeHw01L2V-JXKtrSY1Cc_FDgfBcX1xu21xw3q1iwKyqN_iuY1VvxmvqfzFBS1_wtxeiCO1AN1Q6cCOwSuNqV8cbOMI9LMX9Fp-qgGWGVfBqVCVvCBWuYLGLwqFvp0cQL9UGofxCOCCgVfnDe8aUN_5wH9gru0BCtBhcX1uqLC-JUC'
# (e, t, n) : return "3ce802259e42e6ab081b8fcf78b807ee"
# encrypt : return "aLOBoiuynUYpNqNBfTO06iU8UB2Yk_YBYLF0kiuygqOx"


with open('./zhihu_81_86_encrypt.js') as f:
    # npm 全局安装 jsdom，cwd 指定全局路径
    js = execjs.compile(f.read(), cwd=r'F:\AppData\Roaming\npm\node_modules')
    zse86 = js.call('getResult', paramsJoin)
    print(zse86)
