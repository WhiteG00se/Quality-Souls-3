# -*- coding: utf-8 -*-
def t400200_1():
    """State 0,1"""
    assert GetCurrentStateElapsedTime() > 1
    while True:
        """State 2"""
        call = t400200_x17()
        assert IsClientPlayer()
        """State 3"""
        call = t400200_x18()
        assert not IsClientPlayer()

def t400200_x0(action2=12002003):
    """State 0,1"""
    # action:12002003:"Use <?gdsparam@2141?> to reinforce Estus Flask?"
    OpenGenericDialog(DialogBoxType.CenterBottom2, action2, DialogResult.Leave, DialogBoxStyle.Unk, 2)
    assert not CheckSpecificPersonGenericDialogIsOpen(0)
    """State 2"""
    if GetGenericDialogButtonResult() == DialogResult.Left:
        """State 3"""
        return 0
    else:
        """State 4"""
        return 1

def t400200_x1(actionbutton1=6000, flag7=1175, flag8=1176, flag9=6000, flag10=6000, flag11=6000):
    """State 0"""
    while True:
        """State 1"""
        assert (not GetOneLineHelpStatus() and not IsTalkingToSomeoneElse() and not IsClientPlayer() and not IsPlayerDead()
                and not IsCharacterDisabled())
        """State 3"""
        assert GetEventFlag(flag7) or GetEventFlag(flag8) or GetEventFlag(flag9) or GetEventFlag(flag10) or GetEventFlag(flag11)
        """State 2"""
        if (not (not GetOneLineHelpStatus() and not IsTalkingToSomeoneElse() and not IsClientPlayer() and not IsPlayerDead()
            and not IsCharacterDisabled()) or (not GetEventFlag(flag7) and not GetEventFlag(flag8) and not GetEventFlag(flag9)
            and not GetEventFlag(flag10) and not GetEventFlag(flag11))):
            pass
        elif CheckActionButtonArea(actionbutton1):
            break
    """State 4"""
    return 0

def t400200_x2():
    """State 0,1"""
    if not CheckSpecificPersonTalkHasEnded(0):
        """State 7"""
        ClearTalkProgressData()
        StopEventAnimWithoutForcingConversationEnd(0)
        """State 6"""
        ReportConversationEndToHavokBehavior()
    else:
        pass
    """State 2"""
    if CheckSpecificPersonGenericDialogIsOpen(0):
        """State 3"""
        ForceCloseGenericDialog()
    else:
        pass
    """State 4"""
    if CheckSpecificPersonMenuIsOpen(-1, 0) and not CheckSpecificPersonGenericDialogIsOpen(0):
        """State 5"""
        ForceCloseMenu()
    else:
        pass
    """State 8"""
    return 0

def t400200_x3():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t400200_x4(text3=_, flag5=_, flag6=0, mode3=1):
    """State 0,5"""
    assert t400200_x3() and CheckSpecificPersonTalkHasEnded(0)
    """State 2"""
    SetEventFlag(flag5, FlagState.On)
    """State 1"""
    TalkToPlayer(text3, -1, -1, flag6)
    assert CheckSpecificPersonTalkHasEnded(0)
    """State 4"""
    if mode3 == 0:
        pass
    else:
        """State 3"""
        ReportConversationEndToHavokBehavior()
    """State 6"""
    return 0

def t400200_x5(text2=_, flag3=_, flag4=0, mode2=1):
    """State 0,5"""
    assert t400200_x3() and CheckSpecificPersonTalkHasEnded(0)
    """State 1"""
    TalkToPlayer(text2, -1, -1, flag4)
    assert CheckSpecificPersonTalkHasEnded(0)
    """State 4"""
    if mode2 == 0:
        pass
    else:
        """State 3"""
        ReportConversationEndToHavokBehavior()
    """State 2"""
    SetEventFlag(flag3, FlagState.On)
    """State 6"""
    return 0

def t400200_x6(text1=_, flag2=0, mode1=1):
    """State 0,4"""
    assert t400200_x3() and CheckSpecificPersonTalkHasEnded(0)
    """State 1"""
    TalkToPlayer(text1, -1, -1, flag2)
    assert CheckSpecificPersonTalkHasEnded(0)
    """State 3"""
    if mode1 == 0:
        pass
    else:
        """State 2"""
        ReportConversationEndToHavokBehavior()
    """State 5"""
    return 0

def t400200_x7(lot1=61000):
    """State 0,1"""
    # lot:61000:Hawkwood's Swordgrass
    AwardItemLot(lot1)
    assert not IsMenuOpen(MenuType.Bonfire) and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    return 0

def t400200_x8(gesture1=12, goods8=9002, flag1=6062):
    """State 0,1"""
    if GetEventFlag(flag1):
        """State 2"""
        pass
    else:
        """State 3,4"""
        AcquireGesture(gesture1)
        # goods:9002:Hurrah!
        OpenItemAcquisitionMenu(ItemType.Goods, goods8, 1)
        SetEventFlag(flag1, FlagState.On)
        assert not IsMenuOpen(MenuType.Bonfire) and GetCurrentStateElapsedFrames() > 1
    """State 5"""
    return 0

def t400200_x9(action1=_):
    """State 0,1"""
    OpenGenericDialog(DialogBoxType.CenterBottom1, action1, DialogResult.Left, DialogBoxStyle.OrnateNoOptions, 1)
    assert not CheckSpecificPersonGenericDialogIsOpen(0)
    """State 2"""
    return 0

def t400200_x10(goods5=150, goods7=_):
    """State 0,1"""
    if (not DoesPlayerHaveItem(ItemType.Goods, goods5 + 1 + goods7 * 40 + 0 * 2) and not DoesPlayerHaveItem(ItemType.Goods,
        goods5 + 1 + goods7 * 40 + 1 * 2) and not DoesPlayerHaveItem(ItemType.Goods, goods5 + 1 + goods7 * 40 +
        2 * 2) and not DoesPlayerHaveItem(ItemType.Goods, goods5 + 1 + goods7 * 40 + 3 * 2) and not DoesPlayerHaveItem(ItemType.Goods,
        goods5 + 1 + goods7 * 40 + 4 * 2) and not DoesPlayerHaveItem(ItemType.Goods, goods5 + 1 + goods7 * 40 +
        5 * 2) and not DoesPlayerHaveItem(ItemType.Goods, goods5 + 1 + goods7 * 40 + 6 * 2) and not DoesPlayerHaveItem(ItemType.Goods,
        goods5 + 1 + goods7 * 40 + 7 * 2) and not DoesPlayerHaveItem(ItemType.Goods, goods5 + 1 + goods7 * 40 +
        8 * 2) and not DoesPlayerHaveItem(ItemType.Goods, goods5 + 1 + goods7 * 40 + 9 * 2)):
        """State 2"""
        if (not DoesPlayerHaveItem(ItemType.Goods, goods5 + 1 + goods7 * 40 + 10 * 2) and not DoesPlayerHaveItem(ItemType.Goods,
            goods5 + 1 + goods7 * 40 + 11 * 2) and not DoesPlayerHaveItem(ItemType.Goods, goods5 + 12 + goods7
            * 40 + 12 * 2) and not DoesPlayerHaveItem(ItemType.Goods, goods5 + 1 + goods7 * 40 + 13 * 2) and not
            DoesPlayerHaveItem(ItemType.Goods, goods5 + 1 + goods7 * 40 + 14 * 2) and not DoesPlayerHaveItem(ItemType.Goods,
            goods5 + 1 + goods7 * 40 + 15 * 2) and not DoesPlayerHaveItem(ItemType.Goods, goods5 + 1 + goods7 *
            40 + 16 * 2) and not DoesPlayerHaveItem(ItemType.Goods, goods5 + 1 + goods7 * 40 + 17 * 2) and not
            DoesPlayerHaveItem(ItemType.Goods, goods5 + 1 + goods7 * 40 + 18 * 2) and not DoesPlayerHaveItem(ItemType.Goods,
            goods5 + 1 + goods7 * 40 + 19 * 2)):
            """State 3"""
            if (not DoesPlayerHaveItem(ItemType.Goods, goods5 + 0 + goods7 * 40 + 0 * 2) and not DoesPlayerHaveItem(ItemType.Goods,
                goods5 + 0 + goods7 * 40 + 1 * 2) and not DoesPlayerHaveItem(ItemType.Goods, goods5 + 0 + goods7
                * 40 + 2 * 2) and not DoesPlayerHaveItem(ItemType.Goods, goods5 + 0 + goods7 * 40 + 3 * 2) and
                not DoesPlayerHaveItem(ItemType.Goods, goods5 + 0 + goods7 * 40 + 4 * 2) and not DoesPlayerHaveItem(ItemType.Goods,
                goods5 + 0 + goods7 * 40 + 5 * 2) and not DoesPlayerHaveItem(ItemType.Goods, goods5 + 0 + goods7
                * 40 + 6 * 2) and not DoesPlayerHaveItem(ItemType.Goods, goods5 + 0 + goods7 * 40 + 7 * 2) and
                not DoesPlayerHaveItem(ItemType.Goods, goods5 + 0 + goods7 * 40 + 8 * 2) and not DoesPlayerHaveItem(ItemType.Goods,
                goods5 + 0 + goods7 * 40 + 9 * 2)):
                """State 4"""
                if (not DoesPlayerHaveItem(ItemType.Goods, goods5 + 0 + goods7 * 40 + 10 * 2) and not DoesPlayerHaveItem(ItemType.Goods,
                    goods5 + 0 + goods7 * 40 + 11 * 2) and not DoesPlayerHaveItem(ItemType.Goods, goods5 + 0 +
                    goods7 * 40 + 12 * 2) and not DoesPlayerHaveItem(ItemType.Goods, goods5 + 0 + goods7 * 40 +
                    13 * 2) and not DoesPlayerHaveItem(ItemType.Goods, goods5 + 0 + goods7 * 40 + 14 * 2) and not
                    DoesPlayerHaveItem(ItemType.Goods, goods5 + 0 + goods7 * 40 + 15 * 2) and not DoesPlayerHaveItem(ItemType.Goods,
                    goods5 + 0 + goods7 * 40 + 16 * 2) and not DoesPlayerHaveItem(ItemType.Goods, goods5 + 0 +
                    goods7 * 40 + 17 * 2) and not DoesPlayerHaveItem(ItemType.Goods, goods5 + 0 + goods7 * 40 +
                    18 * 2) and not DoesPlayerHaveItem(ItemType.Goods, goods5 + 0 + goods7 * 40 + 19 * 2)):
                    """State 5"""
                    return 0
                else:
                    pass
            else:
                pass
        else:
            pass
    else:
        pass
    """State 6"""
    return 1

def t400200_x11(goods1=2103, goods2=2104, goods3=2105, goods4=2106, goods5=150, goods6=2141, val1=14):
    """State 0,18"""
    MainBonfireMenuFlag()
    while True:
        """State 1"""
        ClearTalkListData()
        assert (not CheckSpecificPersonGenericDialogIsOpen(2) and not (CheckSpecificPersonMenuIsOpen(-1, 2) and
                not CheckSpecificPersonGenericDialogIsOpen(2)))
        """State 12"""
        # action:15010002:"Reinforce Weapon"
        AddTalkListData(2, 15010002, -1)
        # action:15010001:"Infuse Weapon"
        AddTalkListData(1, 15010001, -1)
        # action:15010003:"Repair Equipment"
        AddTalkListData(3, 15010003, -1)
        # action:15002002:"Allot Estus"
        AddTalkListData(7, 15002002, -1)
        # action:15002003:"Reinforce Estus Flask"
        AddTalkListData(8, 15002003, -1)
        # goods:2103:Farron Coal
        # goods:2104:Sage's Coal
        # goods:2105:Giant's Coal
        # goods:2106:Profaned Coal
        # action:15010000:"Give Coal"
        AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Goods, goods1, CompareType.Greater, 0, False) or ComparePlayerInventoryNumber(ItemType.Goods, goods2, CompareType.Greater, 0, False) or ComparePlayerInventoryNumber(ItemType.Goods, goods3, CompareType.Greater, 0, False) or ComparePlayerInventoryNumber(ItemType.Goods, goods4, CompareType.Greater, 0, False),
                          4, 15010000, -1)
        # action:15000000:"Talk"
        AddTalkListData(5, 15000000, -1)
        # action:15000005:"Leave"
        AddTalkListData(99, 15000005, -1)
        """State 13"""
        ShowShopMessage(TalkOptionsType.Regular)
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) and not CheckSpecificPersonGenericDialogIsOpen(0))
        """State 2"""
        if GetTalkListEntryResult() == 1:
            """State 3,14"""
            CombineMenuFlagAndEventFlag(6001, 344)
            CombineMenuFlagAndEventFlag(6001, 337)
            CombineMenuFlagAndEventFlag(6001, 334)
            CombineMenuFlagAndEventFlag(300, 332)
            CombineMenuFlagAndEventFlag(300, 333)
            CombineMenuFlagAndEventFlag(300, 342)
            CombineMenuFlagAndEventFlag(301, 335)
            CombineMenuFlagAndEventFlag(301, 345)
            CombineMenuFlagAndEventFlag(301, 340)
            CombineMenuFlagAndEventFlag(302, 336)
            CombineMenuFlagAndEventFlag(302, 338)
            CombineMenuFlagAndEventFlag(302, 339)
            CombineMenuFlagAndEventFlag(303, 341)
            CombineMenuFlagAndEventFlag(303, 343)
            CombineMenuFlagAndEventFlag(303, 346)
            CombineMenuFlagAndEventFlag(6000, 347)
            CombineMenuFlagAndEventFlag(6001, 331)
            """State 6"""
            OpenEquipmentChangeOfPurposeShop()
            assert not (CheckSpecificPersonMenuIsOpen(7, 0) and not CheckSpecificPersonGenericDialogIsOpen(0))
        elif GetTalkListEntryResult() == 2:
            """State 4"""
            if GetEventFlag(2051) or IsMultiplayerInProgress():
                """State 21,27"""
                assert t400200_x9(action1=13010000)
            else:
                """State 17"""
                CombineMenuFlagAndEventFlag(6001, 232)
                CombineMenuFlagAndEventFlag(6001, 233)
                CombineMenuFlagAndEventFlag(6001, 234)
                """State 9"""
                OpenEnhanceShop(EnhanceType.Normal)
                assert not (CheckSpecificPersonMenuIsOpen(9, 0) and not CheckSpecificPersonGenericDialogIsOpen(0))
        elif GetTalkListEntryResult() == 3:
            """State 8,10"""
            OpenRepairShop()
            assert not (CheckSpecificPersonMenuIsOpen(8, 0) and not CheckSpecificPersonGenericDialogIsOpen(0))
        elif GetTalkListEntryResult() == 4:
            """State 5,23"""
            assert t400200_x19(goods1=goods1, goods2=goods2, goods3=goods3, goods4=goods4)
        elif GetTalkListEntryResult() == 5:
            """State 11,24"""
            assert t400200_x20()
        elif GetTalkListEntryResult() == 6:
            """State 15,16"""
            OpenRegularShop(100000, 109999)
            assert not (CheckSpecificPersonMenuIsOpen(5, 0) and not CheckSpecificPersonGenericDialogIsOpen(0))
        elif GetTalkListEntryResult() == 7:
            """State 20,26"""
            assert t400200_x24(goods5=goods5) and not (CheckSpecificPersonMenuIsOpen(8, 0) and not CheckSpecificPersonGenericDialogIsOpen(0))
        elif GetTalkListEntryResult() == 8:
            """State 19,25"""
            assert (t400200_x23(goods5=goods5, goods6=goods6, val1=val1) and not (CheckSpecificPersonMenuIsOpen(8,
                    0) and not CheckSpecificPersonGenericDialogIsOpen(0)))
        else:
            """State 7,22"""
            # talk:20000500:"Prithee, be careful."
            # talk:20000501:"I don't want to see m' work squandered!"
            # talk:20000502:" "
            assert t400200_x6(text1=20000500, flag2=0, mode1=1)
            """State 28"""
            return 0

def t400200_x12():
    """State 0,1"""
    if GetEventFlag(1175):
        """State 2"""
        if not GetEventFlag(74000200):
            """State 3,12"""
            # talk:20000000:"Well, a newcomer I see."
            # talk:20000001:"I am Andre. I serve at this shrine."
            # talk:20000002:"As a humble smith, forging weapons."
            # talk:20000003:"You're in search of the Lords of Cinder, I trust?"
            # talk:20000004:"A toilsome journey I'd wager. You'll require good arms."
            # talk:20000005:"Let me smith y' weapons."
            # talk:20000006:"I am a smith, such is my purpose."
            assert t400200_x5(text2=20000000, flag3=74000200, flag4=0, mode2=1)
        elif GetEventFlag(74000201) and not GetEventFlag(74000210):
            """State 5"""
            if not GetEventFlag(50006100):
                """State 7,11"""
                # talk:20001200:"Oh, you've returned. I was hoping to see y'."
                # talk:20001201:"That crestfallen arse Hawkwood, he handed me this."
                # talk:20001202:"He's changed a great deal since he left this place."
                # talk:20001203:"Graven of face, he asked me to give it y'."
                assert t400200_x6(text1=20001200, flag2=0, mode1=1)
                """State 14"""
                # lot:61000:Hawkwood's Swordgrass
                assert t400200_x7(lot1=61000)
            else:
                """State 8"""
                pass
            """State 15"""
            # talk:20001250:"Well, now that that task is concluded..."
            # talk:20001251:"What would y' ha' me smith today?"
            assert t400200_x5(text2=20001250, flag3=74000210, flag4=0, mode2=1)
        else:
            """State 4,10"""
            # talk:20000100:"Ahh, well met."
            # talk:20000101:"Tis good to see y' in good health."
            # talk:20000102:"What needs smithing this day?"
            assert t400200_x6(text1=20000100, flag2=0, mode1=1)
        """State 9"""
        # goods:2103:Farron Coal
        # goods:2104:Sage's Coal
        # goods:2105:Giant's Coal
        # goods:2106:Profaned Coal
        # goods:151:Estus Flask
        # goods:191:Ashen Estus Flask
        # goods:153:Estus Flask+1
        # goods:193:Ashen Estus Flask+1
        # goods:155:Estus Flask+2
        # goods:195:Ashen Estus Flask+2
        # goods:157:Estus Flask+3
        # goods:197:Ashen Estus Flask+3
        # goods:159:Estus Flask+4
        # goods:199:Ashen Estus Flask+4
        # goods:161:Estus Flask+5
        # goods:201:Ashen Estus Flask+5
        # goods:163:Estus Flask+6
        # goods:203:Ashen Estus Flask+6
        # goods:165:Estus Flask+7
        # goods:205:Ashen Estus Flask+7
        # goods:167:Estus Flask+8
        # goods:207:Ashen Estus Flask+8
        # goods:169:Estus Flask+9
        # goods:209:Ashen Estus Flask+9
        # goods:171:Estus Flask+10
        # goods:211:Ashen Estus Flask+10
        # goods:150:Estus Flask
        # goods:190:Ashen Estus Flask
        # goods:152:Estus Flask+1
        # goods:192:Ashen Estus Flask+1
        # goods:154:Estus Flask+2
        # goods:194:Ashen Estus Flask+2
        # goods:156:Estus Flask+3
        # goods:196:Ashen Estus Flask+3
        # goods:158:Estus Flask+4
        # goods:198:Ashen Estus Flask+4
        # goods:160:Estus Flask+5
        # goods:200:Ashen Estus Flask+5
        # goods:162:Estus Flask+6
        # goods:202:Ashen Estus Flask+6
        # goods:164:Estus Flask+7
        # goods:204:Ashen Estus Flask+7
        # goods:166:Estus Flask+8
        # goods:206:Ashen Estus Flask+8
        # goods:168:Estus Flask+9
        # goods:208:Ashen Estus Flask+9
        # goods:170:Estus Flask+10
        # goods:210:Ashen Estus Flask+10
        # goods:2141:Estus Shard
        assert t400200_x11(goods1=2103, goods2=2104, goods3=2105, goods4=2106, goods5=150, goods6=2141, val1=14)
    else:
        """State 6,13"""
        # talk:20001700:"Overstep not yer bounds, cousin."
        # talk:20001701:"I may serve, but I'm no slave."
        # talk:20001702:"I have business I must attend. Be gone."
        assert t400200_x6(text1=20001700, flag2=0, mode1=1)
    """State 16"""
    return 0

def t400200_x13():
    """State 0,9"""
    assert t400200_x2() and GetCurrentStateElapsedFrames() > 1
    """State 1"""
    if GetDistanceToPlayer() < 10:
        """State 2"""
        if not GetEventFlag(74000214):
            """State 6,14"""
            # talk:20001300:" "
            call = t400200_x4(text3=20001300, flag5=74000214, flag6=0, mode3=1)
            if call.Done():
                pass
            elif GetDistanceToPlayer() > 12:
                """State 10"""
                assert t400200_x2()
        elif not GetEventFlag(74000215):
            """State 7,15"""
            # talk:20001400:" "
            call = t400200_x4(text3=20001400, flag5=74000215, flag6=0, mode3=1)
            if call.Done():
                pass
            elif GetDistanceToPlayer() > 12:
                """State 11"""
                assert t400200_x2()
        else:
            """State 8,4"""
            SetEventFlag(74000214, FlagState.Off)
            """State 5"""
            SetEventFlag(74000215, FlagState.Off)
            """State 13"""
            # talk:20001500:"Enough of that!"
            call = t400200_x6(text1=20001500, flag2=0, mode1=1)
            if call.Done():
                pass
            elif GetDistanceToPlayer() > 12:
                """State 12"""
                assert t400200_x2()
    else:
        """State 3"""
        pass
    """State 16"""
    return 0

def t400200_x14():
    """State 0,1"""
    if GetEventFlag(1178):
        """State 2"""
        pass
    else:
        """State 3"""
        if GetDistanceToPlayer() < 10:
            """State 4,7"""
            # talk:20001600:" "
            # talk:20001601:"Beshrew your heart..."
            call = t400200_x6(text1=20001600, flag2=0, mode1=1)
            if call.Done():
                pass
            elif GetDistanceToPlayer() > 12:
                """State 6"""
                assert t400200_x2()
        else:
            """State 5"""
            pass
    """State 8"""
    return 0

def t400200_x15():
    """State 0,3"""
    if GetEventFlag(1176) or GetEventFlag(1177):
        """State 1"""
        if GetDistanceToPlayer() < 10:
            """State 4"""
            pass
        else:
            """State 5"""
            pass
    else:
        """State 2"""
        pass
    """State 6"""
    return 0

def t400200_x16():
    """State 0,1"""
    if CheckSpecificPersonMenuIsOpen(-1, 0) and not CheckSpecificPersonGenericDialogIsOpen(0):
        """State 2,5"""
        # talk:20000500:"Prithee, be careful."
        # talk:20000501:"I don't want to see m' work squandered!"
        # talk:20000502:" "
        call = t400200_x6(text1=20000500, flag2=0, mode1=1)
        if call.Done():
            pass
        elif GetDistanceToPlayer() > 12:
            """State 4"""
            Label('L0')
            assert t400200_x2()
    else:
        """State 3"""
        Goto('L0')
    """State 6"""
    return 0

def t400200_x17():
    """State 0"""
    while True:
        """State 1"""
        call = t400200_x21()
        assert not GetEventFlag(1160)
        """State 2"""
        call = t400200_x22()
        assert GetEventFlag(1160)
    """Unused"""
    """State 3"""
    return 0

def t400200_x18():
    """State 0,1"""
    assert t400200_x2()
    """State 2"""
    return 0

def t400200_x19(goods1=2103, goods2=2104, goods3=2105, goods4=2106):
    """State 0,1"""
    ClearTalkListData()
    """State 17"""
    # goods:2103:Farron Coal
    # action:15010010:"Give <?gdsparam@2103?>"
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Goods, goods1, CompareType.Greater, 0, False), 10,
                      15010010, -1)
    # goods:2104:Sage's Coal
    # action:15010011:"Give <?gdsparam@2104?>"
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Goods, goods2, CompareType.Greater, 0, False), 11,
                      15010011, -1)
    # goods:2105:Giant's Coal
    # action:15010012:"Give <?gdsparam@2105?>"
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Goods, goods3, CompareType.Greater, 0, False), 12,
                      15010012, -1)
    # goods:2106:Profaned Coal
    # action:15010013:"Give <?gdsparam@2106?>"
    AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Goods, goods4, CompareType.Greater, 0, False), 13,
                      15010013, -1)
    # action:15000180:"Quit"
    AddTalkListData(20, 15000180, -1)
    """State 16"""
    ShowShopMessage(TalkOptionsType.Old)
    assert not (CheckSpecificPersonMenuIsOpen(1, 0) and not CheckSpecificPersonGenericDialogIsOpen(0))
    """State 2"""
    if GetTalkListEntryResult() == 10:
        """State 3,8"""
        SetEventFlag(300, FlagState.On)
        """State 9"""
        # goods:2103:Farron Coal
        PlayerEquipmentQuantityChange(ItemType.Goods, goods1, -1)
        """State 18"""
        # talk:20000900:"Oh, my...this coal is from the Undead Legion..."
        # talk:20000901:"Used to forge the weapons of Farron's Abyss Watchers. "
        # talk:20000902:"A fine prize. I'm honoured to be endued with it."
        # talk:20000903:"Now I'll be equipped to infuse special gems."
        # talk:20000904:"Praise the gods, eh. Time to put this brawn to use!"
        # talk:20000905:" "
        assert t400200_x6(text1=20000900, flag2=0, mode1=1)
    elif GetTalkListEntryResult() == 11:
        """State 4,10"""
        SetEventFlag(301, FlagState.On)
        """State 11"""
        # goods:2104:Sage's Coal
        PlayerEquipmentQuantityChange(ItemType.Goods, goods2, -1)
        """State 19"""
        # talk:20001900:"Well, well... What's the Undead Legion doing with a coal such as this?"
        # talk:20001901:"I'd heard one of the Crystal Sages had sided with Farron's Abyss Watchers."
        # talk:20001902:"I suppose it must be true."
        # talk:20001903:"You should know, this coal is imbued with magic. First one I've ever seen."
        # talk:20001904:"Hardly a surprise is it? I've never been one for books or wise men."
        # talk:20001905:" "
        assert t400200_x6(text1=20001900, flag2=0, mode1=1)
    elif GetTalkListEntryResult() == 12:
        """State 5,12"""
        SetEventFlag(302, FlagState.On)
        """State 13"""
        # goods:2105:Giant's Coal
        PlayerEquipmentQuantityChange(ItemType.Goods, goods3, -1)
        """State 20"""
        # talk:20001000:"My, my... The coal of that peaceable giant."
        # talk:20001001:"Seems like ages past. I imagine his passing was long ago."
        # talk:20001002:"I miss the old bugger, I do."
        # talk:20001003:"My thanks. I'll be sure this coal is put to good use."
        # talk:20001004:"I'll be smithing weapons never afore seen by the likes of y'!"
        # talk:20001005:"It's but a small service, to pay my humble respects."
        # talk:20001006:" "
        assert t400200_x6(text1=20001000, flag2=0, mode1=1)
    elif GetTalkListEntryResult() == 13:
        """State 6,14"""
        SetEventFlag(303, FlagState.On)
        """State 15"""
        # goods:2106:Profaned Coal
        PlayerEquipmentQuantityChange(ItemType.Goods, goods4, -1)
        """State 21"""
        # talk:20001100:"Lords... Where didye hap'n upon this coal?"
        # talk:20001101:"This is much too dark. I see the Abyss in it..."
        # talk:20001102:"Yet, a smith I remain. I won't turn down a request."
        # talk:20001103:"But forget not,"
        # talk:20001104:"Your fight is for the flame, and for y' fellow kin. Just like mine."
        # talk:20001105:"A cursed fate this may be, but hope remains, does it not?"
        assert t400200_x6(text1=20001100, flag2=0, mode1=1)
    elif not (CheckSpecificPersonMenuIsOpen(1, 0) and not CheckSpecificPersonGenericDialogIsOpen(0)):
        """State 7"""
        pass
    """State 22"""
    return 0

def t400200_x20():
    """State 0,1"""
    if GetEventFlag(300) and GetEventFlag(301) and GetEventFlag(302):
        """State 2"""
        if not GetEventFlag(74000205):
            """State 4,16"""
            # talk:20000600:"Weapons and protection are sturdy enough, by and large."
            # talk:20000601:"But when overused, they'll eventually break."
            # talk:20000602:"When their durability is low, repair becomes a necessity."
            # talk:20000603:"Use a powder, or simply rest at a bonfire."
            # talk:20000604:"But should chance impel them break, bring them me."
            # talk:20000605:"I'll hammer 'em back into shape."
            # talk:20000606:"They take no pleasure in breaking, I assure y'."
            # talk:20000607:"So, handle them with care, if y' would."
            assert t400200_x5(text2=20000600, flag3=74000205, flag4=0, mode2=1)
        elif not GetEventFlag(74000206):
            """State 5,21"""
            # talk:20000700:"There are two ways to smith weapons."
            # talk:20000701:"Simple reinforcement is one, and infusion the other."
            # talk:20000702:"Reinforcement is straight forward. It strengthens a weapon without altering its property."
            # talk:20000703:"Infusion is a more advanced form of smithing that infuses an element."
            # talk:20000704:"Reinforcement requires titanite, and infusion requires gems."
            # talk:20000705:"Bring the stones, and I'll do the smithing."
            # talk:20000706:"It's m' purpose, after all!"
            # talk:20000707:"In battle, y' weapons are yer only friends. Forge them well, and they won't let y' down."
            assert t400200_x5(text2=20000700, flag3=74000206, flag4=0, mode2=1)
            """State 23"""
            # goods:9002:Hurrah!
            assert t400200_x8(gesture1=12, goods8=9002, flag1=6062)
        else:
            """State 15,20"""
            # talk:20001800:"Oh, by the by."
            # talk:20001801:"If you find any Estus Shards, bring 'em 'ere."
            # talk:20001802:"They can be used to reinforce either of y' Estus Flasks."
            # talk:20001803:"Without those flasks, you'd want for life or focus."
            # talk:20001804:"And they'll always stay with y'. Why not treat 'em well?"
            # talk:20001805:" "
            assert t400200_x6(text1=20001800, flag2=0, mode1=1)
            """State 14"""
            SetEventFlag(74000205, FlagState.Off)
            """State 13"""
            SetEventFlag(74000206, FlagState.Off)
    else:
        """State 3"""
        if not GetEventFlag(74000205):
            """State 6,17"""
            # talk:20000600:"Weapons and protection are sturdy enough, by and large."
            # talk:20000601:"But when overused, they'll eventually break."
            # talk:20000602:"When their durability is low, repair becomes a necessity."
            # talk:20000603:"Use a powder, or simply rest at a bonfire."
            # talk:20000604:"But should chance impel them break, bring them me."
            # talk:20000605:"I'll hammer 'em back into shape."
            # talk:20000606:"They take no pleasure in breaking, I assure y'."
            # talk:20000607:"So, handle them with care, if y' would."
            assert t400200_x5(text2=20000600, flag3=74000205, flag4=0, mode2=1)
        elif not GetEventFlag(74000206):
            """State 7,18"""
            # talk:20000700:"There are two ways to smith weapons."
            # talk:20000701:"Simple reinforcement is one, and infusion the other."
            # talk:20000702:"Reinforcement is straight forward. It strengthens a weapon without altering its property."
            # talk:20000703:"Infusion is a more advanced form of smithing that infuses an element."
            # talk:20000704:"Reinforcement requires titanite, and infusion requires gems."
            # talk:20000705:"Bring the stones, and I'll do the smithing."
            # talk:20000706:"It's m' purpose, after all!"
            # talk:20000707:"In battle, y' weapons are yer only friends. Forge them well, and they won't let y' down."
            assert t400200_x5(text2=20000700, flag3=74000206, flag4=0, mode2=1)
            """State 24"""
            # goods:9002:Hurrah!
            assert t400200_x8(gesture1=12, goods8=9002, flag1=6062)
        elif not GetEventFlag(74000207):
            """State 8,22"""
            # talk:20000800:"Ahh, another matter."
            # talk:20000801:"Infusing weapons with gems requires a special kind of coal."
            # talk:20000802:"My humble coals won't be any use infusing more unusual gems."
            # talk:20000803:"I know, it's an awful shame, but it's all I have."
            # talk:20000804:"Oh, please, don't give me that look."
            # talk:20000805:"Believe it or not, I'm quite thin-skinned."
            # talk:20000806:" "
            assert t400200_x5(text2=20000800, flag3=74000207, flag4=0, mode2=1)
        else:
            """State 9,19"""
            # talk:20001800:"Oh, by the by."
            # talk:20001801:"If you find any Estus Shards, bring 'em 'ere."
            # talk:20001802:"They can be used to reinforce either of y' Estus Flasks."
            # talk:20001803:"Without those flasks, you'd want for life or focus."
            # talk:20001804:"And they'll always stay with y'. Why not treat 'em well?"
            # talk:20001805:" "
            assert t400200_x6(text1=20001800, flag2=0, mode1=1)
            """State 11"""
            SetEventFlag(74000205, FlagState.Off)
            """State 10"""
            SetEventFlag(74000206, FlagState.Off)
            """State 12"""
            SetEventFlag(74000207, FlagState.Off)
    """State 25"""
    return 0

def t400200_x21():
    """State 0,1"""
    call = t400200_x26()
    assert CheckSelfDeath()
    """State 2"""
    t400200_x14()
    Quit()
    """Unused"""
    """State 3"""
    return 0

def t400200_x22():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

def t400200_x23(goods5=150, goods6=2141, val1=14):
    """State 0,18"""
    # goods:151:Estus Flask
    # goods:153:Estus Flask+1
    # goods:155:Estus Flask+2
    # goods:157:Estus Flask+3
    # goods:159:Estus Flask+4
    # goods:161:Estus Flask+5
    # goods:163:Estus Flask+6
    # goods:165:Estus Flask+7
    # goods:167:Estus Flask+8
    # goods:169:Estus Flask+9
    # goods:171:Estus Flask+10
    # goods:150:Estus Flask
    # goods:152:Estus Flask+1
    # goods:154:Estus Flask+2
    # goods:156:Estus Flask+3
    # goods:158:Estus Flask+4
    # goods:160:Estus Flask+5
    # goods:162:Estus Flask+6
    # goods:164:Estus Flask+7
    # goods:166:Estus Flask+8
    # goods:168:Estus Flask+9
    # goods:170:Estus Flask+10
    call = t400200_x10(goods5=goods5, goods7=0)
    if call.Get() == 1:
        """State 10,19"""
        # goods:191:Ashen Estus Flask
        # goods:193:Ashen Estus Flask+1
        # goods:195:Ashen Estus Flask+2
        # goods:197:Ashen Estus Flask+3
        # goods:199:Ashen Estus Flask+4
        # goods:201:Ashen Estus Flask+5
        # goods:203:Ashen Estus Flask+6
        # goods:205:Ashen Estus Flask+7
        # goods:207:Ashen Estus Flask+8
        # goods:209:Ashen Estus Flask+9
        # goods:211:Ashen Estus Flask+10
        # goods:190:Ashen Estus Flask
        # goods:192:Ashen Estus Flask+1
        # goods:194:Ashen Estus Flask+2
        # goods:196:Ashen Estus Flask+3
        # goods:198:Ashen Estus Flask+4
        # goods:200:Ashen Estus Flask+5
        # goods:202:Ashen Estus Flask+6
        # goods:204:Ashen Estus Flask+7
        # goods:206:Ashen Estus Flask+8
        # goods:208:Ashen Estus Flask+9
        # goods:210:Ashen Estus Flask+10
        call = t400200_x10(goods5=goods5, goods7=1)
        if call.Get() == 1:
            """State 12,9"""
            if GetEstusAllocation(EstusType.HP) + GetEstusAllocation(EstusType.FP) < val1:
                """State 1"""
                # goods:2141:Estus Shard
                if ComparePlayerInventoryNumber(ItemType.Goods, goods6, CompareType.Greater, 0, False):
                    """State 2,14"""
                    # action:12002003:"Use <?gdsparam@2141?> to reinforce Estus Flask?"
                    call = t400200_x0(action2=12002003)
                    if call.Get() == 0:
                        """State 4,6"""
                        # goods:2141:Estus Shard
                        PlayerEquipmentQuantityChange(ItemType.Goods, goods6, -1)
                        """State 7"""
                        EstusAllocationUpdate(GetEstusAllocation(EstusType.HP) + 1, 0)
                        """State 16"""
                        # action:13002010:"Reinforced Estus Flask, increasing number of uses\n"
                        assert t400200_x9(action1=13002010)
                        """State 22"""
                        assert t400200_x25(val1=val1)
                    elif call.Done():
                        """State 5"""
                        pass
                else:
                    """State 3,15"""
                    # action:13002011:"No <?gdsparam@2141?> in inventory"
                    assert t400200_x9(action1=13002011)
            else:
                """State 8,17"""
                # action:13002012:"Cannot reinforce further"
                assert t400200_x9(action1=13002012)
        elif call.Done():
            """State 13,21"""
            # action:13002014:"No <?gdsparam@190?> in inventory"
            assert t400200_x9(action1=13002014)
    elif call.Done():
        """State 11,20"""
        # action:13002013:"No <?gdsparam@150?> in inventory"
        assert t400200_x9(action1=13002013)
    """State 23"""
    return 0

def t400200_x24(goods5=150):
    """State 0,6"""
    # goods:151:Estus Flask
    # goods:153:Estus Flask+1
    # goods:155:Estus Flask+2
    # goods:157:Estus Flask+3
    # goods:159:Estus Flask+4
    # goods:161:Estus Flask+5
    # goods:163:Estus Flask+6
    # goods:165:Estus Flask+7
    # goods:167:Estus Flask+8
    # goods:169:Estus Flask+9
    # goods:171:Estus Flask+10
    # goods:150:Estus Flask
    # goods:152:Estus Flask+1
    # goods:154:Estus Flask+2
    # goods:156:Estus Flask+3
    # goods:158:Estus Flask+4
    # goods:160:Estus Flask+5
    # goods:162:Estus Flask+6
    # goods:164:Estus Flask+7
    # goods:166:Estus Flask+8
    # goods:168:Estus Flask+9
    # goods:170:Estus Flask+10
    call = t400200_x10(goods5=goods5, goods7=0)
    if call.Get() == 1:
        """State 1,7"""
        # goods:191:Ashen Estus Flask
        # goods:193:Ashen Estus Flask+1
        # goods:195:Ashen Estus Flask+2
        # goods:197:Ashen Estus Flask+3
        # goods:199:Ashen Estus Flask+4
        # goods:201:Ashen Estus Flask+5
        # goods:203:Ashen Estus Flask+6
        # goods:205:Ashen Estus Flask+7
        # goods:207:Ashen Estus Flask+8
        # goods:209:Ashen Estus Flask+9
        # goods:211:Ashen Estus Flask+10
        # goods:190:Ashen Estus Flask
        # goods:192:Ashen Estus Flask+1
        # goods:194:Ashen Estus Flask+2
        # goods:196:Ashen Estus Flask+3
        # goods:198:Ashen Estus Flask+4
        # goods:200:Ashen Estus Flask+5
        # goods:202:Ashen Estus Flask+6
        # goods:204:Ashen Estus Flask+7
        # goods:206:Ashen Estus Flask+8
        # goods:208:Ashen Estus Flask+9
        # goods:210:Ashen Estus Flask+10
        call = t400200_x10(goods5=goods5, goods7=1)
        if call.Get() == 1:
            """State 3,4"""
            OpenEstusAllotMenu()
            assert not (CheckSpecificPersonMenuIsOpen(14, 0) and not CheckSpecificPersonGenericDialogIsOpen(0))
        elif call.Done():
            """State 5,9"""
            # action:13002014:"No <?gdsparam@190?> in inventory"
            assert t400200_x9(action1=13002014)
    elif call.Done():
        """State 2,8"""
        # action:13002013:"No <?gdsparam@150?> in inventory"
        assert t400200_x9(action1=13002013)
    """State 10"""
    return 0

def t400200_x25(val1=14):
    """State 0,3"""
    if GetEstusAllocation(EstusType.HP) + GetEstusAllocation(EstusType.FP) < val1:
        """State 2"""
        pass
    else:
        """State 1,4"""
        RequestUnlockTrophy(Trophy.UltimateEstus)
    """State 5"""
    return 0

def t400200_x26():
    """State 0"""
    while True:
        """State 5"""
        call = t400200_x1(actionbutton1=6000, flag7=1175, flag8=1176, flag9=6000, flag10=6000, flag11=6000)
        if call.Done():
            """State 3"""
            call = t400200_x12()
            if call.Done():
                pass
            elif IsAttackedBySomeone():
                """State 1"""
                Label('L0')
                call = t400200_x13()
                def ExitPause():
                    RemoveMyAggro()
                if call.Done():
                    pass
                elif IsPlayerDead():
                    break
            elif IsPlayerDead():
                break
            elif GetDistanceToPlayer() > 5:
                """State 4"""
                call = t400200_x16()
                if call.Done() and GetDistanceToPlayer() < 4.9:
                    pass
                elif IsAttackedBySomeone():
                    Goto('L0')
        elif IsAttackedBySomeone():
            Goto('L0')
        elif IsPlayerDead():
            break
    """State 2"""
    t400200_x15()
    Quit()
    """Unused"""
    """State 6"""
    return 0

