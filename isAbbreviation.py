def isAbbreviation(a: str, b: str) -> bool:
    if not a and not b:
        return True
    if not a or not b or len(a) < len(b):
        return False

    isValid = [[False for _ in range(0, len(b) + 1)] for _ in range(0, len(a) + 1)]
    isValid[0][0] = True
    for i in range(0, len(a)):
        for j in range(0, len(b) + 1):
            if isValid[i][j]:
                if j < len(b) and str.upper(a[i]) == b[j]:
                    isValid[i + 1][j + 1] = True
                if str.islower(a[i]):
                    isValid[i + 1][j] = True
    return isValid[len(a)][len(b)]

def testCore(a: str, b: str) -> None:
    print(isAbbreviation(a, b))

def test1() -> None:
    # Yes
    testCore("daBcd", "ABC")

def test2() -> None:
    # No
    testCore("sYOCa", "YOCN")

def test3() -> None:
    # No
    testCore("KXzQ", "K")

def test4() -> None:
    # No
    testCore(
        "RDWPJPAMKGRIWAPBZSYWALDBLDOFLWIQPMPLEMCJXKAENTLVYMSJNRJAQQPWAGVcGOHEWQYZDJRAXZOYDMNZJVUSJGKKKSYNCSFWKVNHOGVYULALKEBUNZHERDDOFCYWBUCJGbvqlddfazmmohcewjg", 
        "RDPJPAMKGRIWAPBZSYWALDBLOFWIQPMPLEMCJXKAENTLVYMJNRJAQQPWAGVGOHEWQYZDJRAXZOYDMNZJVUSJGKKKSYNCSFWKVNHOGVYULALKEBUNZHERDOFCYWBUCJG"
    )

def test5() -> None:
    # No
    testCore(
        "MBQEVZPBjcbswirgrmkkfvfvcpiukuxlnxkkenqp",
        "MBQEVZP"
    )

def test6() -> None:
    # Yes
    testCore(
        "hHhAhhcahhacaccacccahhchhcHcahaahhchhhchaachcaCchhchcaccccchhhcaahhhhcaacchccCaahhaahachhacaahhaachhhaaaCalhhchaccaAahHcchcazhachhhaaahaahhaacchAahccacahahhcHhccahaachAchahacaahcahacaahcahacaHhccccaahaahacaachcchhahhacchahhhaahcacacachhahchcaAhhcaahchHhhaacHcacahaccccaaahacCHhChchhhahhchcahaaCccccahhcaachhhacaaahcaaaccccaacaaHachaahcchaahhchhhcahahahhcaachhchacahhahahahAahaAcchahaahcaaaaahhChacahcacachacahcchHcaahchhcahaachnachhhhcachchahhhacHhCcaHhhhcaCccccaaahcahacahchahcaachcchaachahhhhhhhhcahhacacCcchahccaaaaaHhhccaAaaaCchahhccaahhacaccchhcahhcahaahhgacahcahhchcaaAccchahhhaahhccaaHcchaccacahHahChachhcaaacAhacacaacacchhchchacchchcacchachacaahachccchhhaccahcacchaccaahaaaccccccaaaaaaaHhcahcchmcHchcchaaahaccchaaachchHahcaccaaccahcacacahAhaacaacaccaccaaacahhhcacAhaCchcaacCcccachhchchcchhchahchchahchchhchcacaachahhccacachaAhaaachchhchchchhaachahaahahachhaaaccacahhcacchhhaaachaaacAahhcachchachhhcacchacaaChCahhhccahChaachhcahacchanaaacchhhccacacchcahccchAcahacaaachhacchachccaaHacaacAhahcCh",
        "HAHHCHAACCCAHCHHAHHAHCACCHCCHHCAAHHCACCCAHHHACAAHHHHCHHCAHHAHHAAAHAACAAHAHHCAHAHACHACHCHACACHAAHHAAAHCAHHACACAACHHHCHAHCAHCHHHAHAHACCAAAHCHHCHHCCAACCCCAACHACAACAAHACHCHAHHACCHCAHHHAAACHACAACHCACACAHHCCHAHACCCACCAACHCHHHCCCCCHCCAHHCAAHHAHHHHHHHAACCCCAHCCAAAAAHHHAAAACCAHHCAHACACCHHCHAHAHHCHAACHHHHHCCHCCAHAHCHCAAACCACCCCHACCACHHACHHACACHACCAACCCCAAAAHHAHCHHHCCAHCCHACHHAHCCACACCHAHAAACACCCCAHCCAHACCCCCCHCCHHCHHHHCHCHCAHHHACHAHAACCCAAAACHAACAAAHHAAHAAAHACHHCACHCCHCHAACHACACHHCCCCCAHCACHAAAHCHCAHACAAC"
    )

def test7() -> None:
    # No
    testCore(
        "XbxxobxBobbbxooXobXxxBOXoOboxxbobXOoBbxbXooXBboxooOxxXbboxoOxlobbObbXoXXbbXobbbXoxbxXBxoobooxbxoxoxOxxOxbxbxXobbbbBbxoxoooxooobXxbooBbOXxXxbxqobbbboXxoXXbbbxObXXxobOXXOxoOoxoXOXBxOxBoxbobxoBxbobobXooOxxOBXbxxXbooxbxooOxoxoobxxBOxxbbbxBxzXxbBxOobBObooofbbBXXOxxoxxbXBbOboxxooBbxOoboXoooXBbBbooOoBbbObxobxbBBoOxoxobBoOXXobObxobxOObobbbxxoboxoXxbXoxxxxbbobbXoXooBXXxboxbobxxxXboxOoOoxBoboOXboBoobXobxXdxObbbBxbxBbOOXbxooXboxboonxxxXOBbbXXoobooxbbxboxoOxBBbxBOxoobXbbxxbXXObxBbxBXBxoxOxoBbxBobOXbboxooBxbooXbXbooBbbxXboxXbxXoxbboxOXOooXbobooXXoxobbxoOxOoBbxxoBboboxoOBBxoboBoOboxbbxxbbbObXbboXbObOjXOXBxbxXobbbboBxBoOooxbxxOooxxbxxobbobxbbXoOobbBXoObxobXxoobxBxBbxoobXxoxObboxobobooxOoooBBbbbxxXoxbXxoXooxOBxboobxooxXOxobXoXmObxxXObooXXXboOXxbXxObxxbbObObxbxxbxxBXxBxoxOooaxooxXBXoXOxoOXxbBoBXxXooboXboOooxoxOxXxbxoboOObbBoXxbboxxooBBbooxXBbBoxBOobbboobobooxoxOxoXOXXboxXOboBxoboOooxbxBxobooXOoxOOObbxbobxxoxbOBoBxboxoobbbxoooxBxoobBbobBbooOBbxoboooookxXoobbbbBbOoxOBOobXObXBxoXoboxobbXBXBBoxBxoxooOxobxo",
        "XBOBBOBOXOXBOXOOBOXOXOBBXOXBXOXXBBOBXOXXXOBBXBOOOXXOXBBBXOXOOOXXOBBOXXOBBXXXOXXXOXXOOXOXBOBBBXBBXOOXOBXXOOOOBXBOXXBXBXXXBXOBBOBBXXOXXBOBBXOXXBBOOOBBBOXBBBOXXBXXOBOBXOOOXXXXXXOBXXBOXXOOOOBOOOXBBOOBXOXXOBBBBOOXXOOXXXOBBXXOXBBOXOXBBBOXOBXXXBXXOBBXBOOBBBOXBBBOXBXBOBBXXXOXBOOXOOXBOXXOOOOBBBBOOBBOBOOBOBXBBOXBOBOXOXBXOBBOBBOXBOOXXBBBBBXOBXOBXXXBBBXOOBOOOXOOBBBXXOXXOXOBOXOBXXOXOOXXXOXXOBOOXBBXBOXBXXOXOXBOBXXOOXOOOXXBOOBBXXXBBOXBBXBOBBOOBOOXOXXBXOBOOOXBOXOOXOOOBBOBBOOOBBBBBOOBOXBBBOBOBXOXBXOBXBXBXBBBXOOO"
    )

test1()
test2()
test3()
test4()
test5()
test6()
test7()