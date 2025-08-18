# -*- coding: utf-8 -*-
def t400120_1():
    """State 0,1"""
    assert GetCurrentStateElapsedTime() > 1
    while True:
        """State 2"""
        call = t400120_x14()
        assert IsClientPlayer()
        """State 3"""
        call = t400120_x15()
        assert not IsClientPlayer()

def t400120_x0(action2=_):
    """State 0,1"""
    OpenGenericDialog(DialogBoxType.CenterBottom2, action2, DialogResult.Leave, DialogBoxStyle.Unk, 2)
    assert not CheckSpecificPersonGenericDialogIsOpen(0)
    """State 2"""
    if GetGenericDialogButtonResult() == DialogResult.Left:
        """State 3"""
        return 0
    else:
        """State 4"""
        return 1

def t400120_x1(actionbutton1=6120, flag6=1015, flag7=6000, flag8=6000, flag9=6000, flag10=6000):
    """State 0"""
    while True:
        """State 1"""
        assert (not GetOneLineHelpStatus() and not IsTalkingToSomeoneElse() and not IsClientPlayer() and not IsPlayerDead()
                and not IsCharacterDisabled())
        """State 3"""
        assert GetEventFlag(flag6) or GetEventFlag(flag7) or GetEventFlag(flag8) or GetEventFlag(flag9) or GetEventFlag(flag10)
        """State 2"""
        if (not (not GetOneLineHelpStatus() and not IsTalkingToSomeoneElse() and not IsClientPlayer() and not IsPlayerDead()
            and not IsCharacterDisabled()) or (not GetEventFlag(flag6) and not GetEventFlag(flag7) and not GetEventFlag(flag8)
            and not GetEventFlag(flag9) and not GetEventFlag(flag10))):
            pass
        elif CheckActionButtonArea(actionbutton1):
            break
    """State 4"""
    return 0

def t400120_x2():
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

def t400120_x3():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t400120_x4(text3=12002600, flag4=74000115, flag5=0, mode3=1):
    """State 0,5"""
    assert t400120_x3() and CheckSpecificPersonTalkHasEnded(0)
    """State 2"""
    SetEventFlag(flag4, FlagState.On)
    """State 1"""
    # talk:12002600:" "
    TalkToPlayer(text3, -1, -1, flag5)
    assert CheckSpecificPersonTalkHasEnded(0)
    """State 4"""
    if mode3 == 0:
        pass
    else:
        """State 3"""
        ReportConversationEndToHavokBehavior()
    """State 6"""
    return 0

def t400120_x5(text2=_, flag2=_, flag3=0, mode2=0):
    """State 0,5"""
    assert t400120_x3() and CheckSpecificPersonTalkHasEnded(0)
    """State 1"""
    TalkToPlayer(text2, -1, -1, flag3)
    assert CheckSpecificPersonTalkHasEnded(0)
    """State 4"""
    if mode2 == 0:
        pass
    else:
        """State 3"""
        ReportConversationEndToHavokBehavior()
    """State 2"""
    SetEventFlag(flag2, FlagState.On)
    """State 6"""
    return 0

def t400120_x6(text1=_, flag1=0, mode1=_):
    """State 0,4"""
    assert t400120_x3() and CheckSpecificPersonTalkHasEnded(0)
    """State 1"""
    TalkToPlayer(text1, -1, -1, flag1)
    assert CheckSpecificPersonTalkHasEnded(0)
    """State 3"""
    if mode1 == 0:
        pass
    else:
        """State 2"""
        ReportConversationEndToHavokBehavior()
    """State 5"""
    return 0

def t400120_x7(action1=_):
    """State 0,1"""
    OpenGenericDialog(DialogBoxType.CenterBottom1, action1, DialogResult.Left, DialogBoxStyle.OrnateNoOptions, 1)
    assert not CheckSpecificPersonGenericDialogIsOpen(0)
    """State 2"""
    return 0

def t400120_x8(goods1=2138, goods2=390):
    """State 0,8"""
    MainBonfireMenuFlag()
    while True:
        """State 1"""
        ClearTalkListData()
        """State 2"""
        # action:15002000:"Level Up"
        AddTalkListData(1, 15002000, -1)
        # action:15027010:"Reallocate attributes"
        AddTalkListData(2, 15027010, -1)
        # action:15027011:"Alter appearance"
        AddTalkListData(3, 15027011, -1)
        # action:15002004:"Heal the Dark Sigil"
        AddTalkListDataIf(GetEventFlag(74000125), 4, 15002004, -1)
        # goods:2138:Eyes of a Fire Keeper
        # action:15002001:"Give <?gdsparam@2138?>"
        AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Goods, goods1, CompareType.Greater, 0, False),
                          10, 15002001, -1)
        # goods:390:Fire Keeper Soul
        # action:15002005:"Give <?gdsparam@390?>"
        AddTalkListDataIf(ComparePlayerInventoryNumber(ItemType.Goods, goods2, CompareType.Greater, 0, False),
                          11, 15002005, -1)
        # action:15000000:"Talk"
        AddTalkListData(20, 15000000, -1)
        # action:15000005:"Leave"
        AddTalkListData(99, 15000005, -1)
        assert (not CheckSpecificPersonGenericDialogIsOpen(2) and not (CheckSpecificPersonMenuIsOpen(-1, 2) and
                not CheckSpecificPersonGenericDialogIsOpen(2)))
        """State 3"""
        ShowShopMessage(TalkOptionsType.Regular)
        if GetTalkListEntryResult() == 1:
            """State 4"""
            if GetEventFlag(2051) or IsMultiplayerInProgress():
                pass
            else:
                """State 13"""
                # talk:12000200:"Very well."
                # talk:12000201:"Then touch the darkness within me."
                # talk:12000202:"Take nourishment from these sovereignless souls."
                assert t400120_x6(text1=12000200, flag1=0, mode1=0)
                """State 11"""
                def WhilePaused():
                    SetTalkTime(0.1)
                assert not GetEventFlag(74000137) and not GetEventFlag(74000138)
                """State 19"""
                SetEventFlag(74000135, FlagState.On)
                call = t400120_x25()
                def ExitPause():
                    SetEventFlag(74000135, FlagState.Off)
                    SetEventFlag(74000136, FlagState.Off)
                if call.Get() == 1:
                    """State 21"""
                    Label('L0')
                    return 0
                elif call.Done():
                    continue
        elif GetTalkListEntryResult() == 11:
            """State 5,17"""
            assert t400120_x22(goods2=goods2)
            continue
        elif GetTalkListEntryResult() == 20:
            """State 7,15"""
            assert t400120_x20()
            continue
        elif not (CheckSpecificPersonMenuIsOpen(1, 0) and not CheckSpecificPersonGenericDialogIsOpen(0)):
            """State 6,14"""
            assert t400120_x19()
            Goto('L0')
        elif GetTalkListEntryResult() == 10:
            """State 9,16"""
            def ExitPause():
                SetEventFlag(74000122, FlagState.Off)
            assert t400120_x21(goods1=goods1)
            continue
        elif GetTalkListEntryResult() == 4:
            """State 10"""
            if GetEventFlag(2051) or IsMultiplayerInProgress():
                pass
            else:
                """State 18"""
                # goods:490:Dark Sigil
                assert t400120_x23(goods3=490, z1=0)
                continue
        elif GetTalkListEntryResult() == 2:
            """State 22,23"""
            # This dialog text may mention Pale Tongues and limits, but the functionality is free and unlimited.
            # action:12027020:"...Do you wish to be reborn?"
            call = t400120_x0(action2=12027020)
            if call.Get() == 0:
                # Confirmed. The following flags handle camera/animations for the menu.
                SetEventFlag(73500161, FlagState.On)
                SetEventFlag(73500162, FlagState.On)
                assert GetCurrentStateElapsedTime() > 3
                SetEventFlag(73500164, FlagState.On)
                assert GetCurrentStateElapsedTime() > 1
                
                ReallocateAttributes()
                ClearTalkActionState()
                
                def ExitPause():
                    SetEventFlag(73500161, FlagState.Off)
                
                assert not (CheckSpecificPersonMenuIsOpen(19, 0) and not CheckSpecificPersonGenericDialogIsOpen(0))
                
                SetEventFlag(73500164, FlagState.Off)
                
                assert GetCurrentStateElapsedTime() > 1.5
            elif call.Done():
                # Cancelled
                pass
            continue
        elif GetTalkListEntryResult() == 3:
            """State 24,25"""
            # This dialog text may mention Pale Tongues and limits, but the functionality is free and unlimited.
            # action:12027021:"...Do you wish to be reborn?"
            call = t400120_x0(action2=12027021)
            if call.Get() == 0:
                # Confirmed. The following flags handle camera/animations for the menu.
                SetEventFlag(73500161, FlagState.On)
                SetEventFlag(73500162, FlagState.On)
                assert GetCurrentStateElapsedTime() > 3
                SetEventFlag(73500164, FlagState.On)
                assert GetCurrentStateElapsedTime() > 1
                
                OpenCharaMakeMenu()
                ClearTalkActionState()
                
                def ExitPause():
                    SetEventFlag(73500161, FlagState.Off)
                
                assert not (CheckSpecificPersonMenuIsOpen(16, 0) and not CheckSpecificPersonGenericDialogIsOpen(0))
                
                SetEventFlag(73500164, FlagState.Off)
                
                assert GetCurrentStateElapsedTime() > 1.5
            elif call.Done():
                # Cancelled
                pass
            continue
        """State 12,20"""
        assert t400120_x7(action1=13002040)

def t400120_x9():
    """State 0,1"""
    if GetEventFlag(1002):
        """State 8"""
        if GetEventFlag(74000121):
            """State 11"""
            Label('L0')
            """State 20"""
            # talk:12003150:"I'm truly sorry."
            # talk:12003151:"But, know'st thou not? I cannot die."
            # talk:12003152:"So please, ashen one, allow me to serve thee."
            assert t400120_x6(text1=12003150, flag1=0, mode1=0)
            """State 6"""
            Label('L1')
            SetEventFlag(74000121, FlagState.Off)
        elif GetEventFlag(50006020):
            """State 12,22"""
            # talk:12002000:"Ashen one, link the fire."
            # talk:12002001:"For the Lords of Cinder, for the ashen prisoners,\nfor all those held to preserve the fire."
            # talk:12002002:"Link the First Flame."
            assert t400120_x6(text1=12002000, flag1=0, mode1=0)
        else:
            """State 13,21"""
            # talk:12002200:"Ashen one, if, when thou peerest upon the First Flame..."
            # talk:12002201:"...Thou wishest yet, for a world without fire, for an end to the linking of the fire..."
            # talk:12002202:"Then call upon me."
            # talk:12002203:"I am a Fire Keeper, and I tend to the flame, to the very end."
            # talk:12002204:"Thou'st given me eyes, and such it was they shewed me."
            assert t400120_x6(text1=12002200, flag1=0, mode1=0)
    elif GetEventFlag(1001):
        """State 7"""
        if GetEventFlag(74000121):
            Goto('L0')
        elif not GetEventFlag(74000101):
            """State 9,19"""
            # talk:12001300:"The five lords sit their five thrones."
            # talk:12001301:"All thanks to thee, most worthy of lords."
            # talk:12001302:"Ashen one, with the Lords as thy witness, bend thy knee afore the bonfire's coiled sword."
            # talk:12001303:"And let the Lords' embers acknowledge thee as their true heir."
            # talk:12001304:"A true lord, fit to link the fire."
            assert t400120_x5(text2=12001300, flag2=74000101, flag3=0, mode2=0)
        else:
            """State 10,18"""
            # talk:12001400:"Ashen one, with the Lords as thy witness, bend thy knee afore the bonfire's coiled sword."
            # talk:12001401:"And let the Lords' embers acknowledge thee as their true heir."
            # talk:12001402:"A true lord, fit to link the fire."
            assert t400120_x6(text1=12001400, flag1=0, mode1=0)
    else:
        """State 2"""
        if GetEventFlag(74000121):
            """State 5,17"""
            # talk:12003100:"I'm truly sorry."
            # talk:12003101:"But, know'st thou not? I cannot die."
            # talk:12003102:"So please, ashen one, allow me to serve thee."
            # talk:12003103:"The Lords have left their thrones, and must be delivered to them."
            # talk:12003104:"To this end, I am ever at thy side."
            assert t400120_x6(text1=12003100, flag1=0, mode1=0)
            Goto('L1')
        elif not GetEventFlag(74000100):
            """State 3,16"""
            # talk:12000000:"Welcome to the bonfire, Unkindled One."
            # talk:12000001:"I am a Fire Keeper."
            # talk:12000002:"I tend to the flame, and tend to thee."
            # talk:12000003:"The Lords have left their thrones, and must be deliver'd to them."
            # talk:12000004:"To this end, I am at thy side."
            assert t400120_x5(text2=12000000, flag2=74000100, flag3=0, mode2=0)
        else:
            """State 4"""
            if not GetEventFlag(131):
                """State 23"""
                # talk:12003200:"Ashen one."
                # talk:12003201:"Produce the coiled sword at the bonfire."
                # talk:12003202:"The mark of ash will guide thee to the land of the Lords."
                # talk:12003203:"To Lothric, where the homes of the Lords converge."
                assert t400120_x6(text1=12003200, flag1=0, mode1=0)
            else:
                """State 15"""
                # talk:12000100:"Welcome home, ashen one."
                # talk:12000101:"Speak thine heart's desire."
                assert t400120_x6(text1=12000100, flag1=0, mode1=0)
    """State 14"""
    # goods:2138:Eyes of a Fire Keeper
    # goods:390:Fire Keeper Soul
    assert t400120_x8(goods1=2138, goods2=390)
    """State 24"""
    return 0

def t400120_x10():
    """State 0,6"""
    assert t400120_x2()
    """State 3"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 1"""
    assert not GetEventFlag(1016) and not GetEventFlag(1017)
    """State 2"""
    if GetDistanceToPlayer() < 10:
        """State 4,8"""
        call = t400120_x18()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > 12:
            """State 7"""
            assert t400120_x2()
    else:
        """State 5"""
        pass
    """State 9"""
    return 0

def t400120_x11():
    """State 0,1"""
    if GetEventFlag(1018):
        """State 2"""
        pass
    else:
        """State 3"""
        if GetDistanceToPlayer() < 10:
            """State 4"""
            if GetEventFlag(50006020):
                """State 6,9"""
                # talk:12002900:" "
                # talk:12002901:"Ashen one, what is wrong?"
                call = t400120_x6(text1=12002900, flag1=0, mode1=1)
                if call.Done():
                    Goto('L0')
                elif GetDistanceToPlayer() > 12:
                    pass
            else:
                """State 7,10"""
                # talk:12002950:" "
                call = t400120_x6(text1=12002950, flag1=0, mode1=1)
                if call.Done():
                    Goto('L0')
                elif GetDistanceToPlayer() > 12:
                    pass
            """State 8"""
            assert t400120_x2()
        else:
            """State 5"""
            pass
    """State 11"""
    Label('L0')
    return 0

def t400120_x12():
    """State 0,1,2"""
    assert t400120_x2()
    """State 3"""
    return 0

def t400120_x13():
    """State 0,1"""
    if CheckSpecificPersonMenuIsOpen(-1, 0) and not CheckSpecificPersonMenuIsOpen(12, 0) and not CheckSpecificPersonGenericDialogIsOpen(0):
        """State 2,5"""
        call = t400120_x19()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > 12:
            """State 4"""
            Label('L0')
            assert t400120_x2()
    else:
        """State 3"""
        Goto('L0')
    """State 6"""
    return 0

def t400120_x14():
    """State 0"""
    while True:
        """State 1"""
        call = t400120_x16()
        assert not GetEventFlag(1000) and not GetEventFlag(1001) and not GetEventFlag(1002)
        """State 2"""
        call = t400120_x17()
        assert GetEventFlag(1000) or GetEventFlag(1001) or GetEventFlag(1002)
    """Unused"""
    """State 3"""
    return 0

def t400120_x15():
    """State 0,1"""
    assert t400120_x2()
    """State 2"""
    return 0

def t400120_x16():
    """State 0,1"""
    call = t400120_x26()
    assert CheckSelfDeath()
    """State 2"""
    t400120_x11()
    Quit()
    """Unused"""
    """State 3"""
    return 0

def t400120_x17():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

def t400120_x18():
    """State 0,1"""
    if not GetEventFlag(74000115):
        """State 2,5"""
        # talk:12002600:" "
        assert t400120_x4(text3=12002600, flag4=74000115, flag5=0, mode3=1)
    else:
        """State 3,6"""
        # talk:12002700:" "
        assert t400120_x6(text1=12002700, flag1=0, mode1=1)
        """State 4"""
        SetEventFlag(74000115, FlagState.Off)
    """State 7"""
    return 0

def t400120_x19():
    """State 0,1"""
    if GetEventFlag(1002):
        """State 5"""
        if GetEventFlag(50006020):
            """State 6,10"""
            # talk:12002100:"Ashen one, may the flames guide thee."
            assert t400120_x6(text1=12002100, flag1=0, mode1=1)
        else:
            """State 7,11"""
            # talk:12002300:"Mayst thou thy peace discov'r."
            assert t400120_x6(text1=12002300, flag1=0, mode1=1)
    else:
        """State 2"""
        if GetEventFlag(50006020):
            """State 3,8"""
            # talk:12000400:"Farewell, ashen one."
            # talk:12000401:"May the flames guide thee."
            assert t400120_x6(text1=12000400, flag1=0, mode1=1)
        else:
            """State 4,9"""
            # talk:12000500:"Farewell, ashen one."
            # talk:12000501:"Mayst thou thy peace discov'r."
            assert t400120_x6(text1=12000500, flag1=0, mode1=1)
    """State 12"""
    return 0

def t400120_x20():
    """State 0,1"""
    if GetEventFlag(50006020):
        """State 2"""
        if GetEventFlag(9300) and not GetEventFlag(1002):
            """State 4,20"""
            # talk:12000700:"Ashen one, may I pose thee a question?"
            # talk:12000701:"Has the little Lord Ludleth spoken to thee of any...curious matters?"
            # talk:12000702:"I sense that he possesseth some knowledge..."
            # talk:12000703:"Of a thing once most precious, or most terrible, now lost to the Fire Keepers."
            # talk:12000704:"Pray tell, is it a matter of which I should be apprised?"
            assert t400120_x6(text1=12000700, flag1=0, mode1=0)
        else:
            """State 3,19"""
            # talk:12000600:"Ashen one, to be unkindled is to be a vessel for souls."
            # talk:12000601:"Sovereignless souls will become thy strength."
            # talk:12000602:"I will show thee how."
            # talk:12000603:"Ashen one, bring me souls, plucked from their vessels..."
            assert t400120_x6(text1=12000600, flag1=0, mode1=0)
    else:
        """State 5"""
        if not GetEventFlag(74000130) and not GetEventFlag(74000131):
            """State 7,21"""
            # talk:12000800:"Ashen one, my thanks for the eyes thou'st given."
            # talk:12000801:"But Fire Keepers are not meant to have eyes. It is forbidden."
            # talk:12000802:"These will reveal, through a sliver of light, frightful images of betrayal."
            # talk:12000803:"A world without fire."
            # talk:12000804:"Ashen one, is this truly thy wish?"
            assert (t400120_x6(text1=12000800, flag1=0, mode1=0) and (not CheckSpecificPersonGenericDialogIsOpen(2)
                    and not (CheckSpecificPersonMenuIsOpen(-1, 2) and not CheckSpecificPersonGenericDialogIsOpen(2))))
            """State 14"""
            ClearTalkListData()
            """State 15"""
            # action:14002000:"Wish for a world without flame"
            AddTalkListData(1, 14002000, -1)
            # action:14002001:"Decline"
            AddTalkListData(2, 14002001, -1)
            """State 13"""
            OpenConversationChoicesMenu(0)
            assert not (CheckSpecificPersonMenuIsOpen(12, 0) and not CheckSpecificPersonGenericDialogIsOpen(0))
            """State 17"""
            if GetTalkListEntryResult() == 1:
                """State 12,24"""
                # talk:12000900:"Of course."
                # talk:12000901:"I serve thee, and will do as thou bid'st."
                # talk:12000902:"This will be our private affair. No one else may know of this."
                # talk:12000903:"Stay thy path, find lords to link the fire, and I will blindly tend to the flame."
                # talk:12000904:"Until the day of thy grand betrayal."
                assert t400120_x5(text2=12000900, flag2=74000130, flag3=0, mode2=0)
            elif GetTalkListEntryResult() == 2:
                """State 16,25"""
                # talk:12001100:"Of course not."
                # talk:12001101:"Please, kill me, and take these eyes away."
                # talk:12001102:"Before I am drawn into the darkness."
                # talk:12001103:"Seduced by the thin light, and the awful betrayal..."
                assert t400120_x5(text2=12001100, flag2=74000131, flag3=0, mode2=0)
            else:
                """State 18"""
                pass
        else:
            """State 6"""
            if GetEventFlag(74000130):
                """State 8"""
                if not GetEventFlag(74000132) or GetEventFlag(74000110):
                    """State 10,23"""
                    # talk:12001000:"Ashen one, if thine heart should bend..."
                    # talk:12001001:"...kill me, and strip these eyes from my person."
                    # talk:12001002:"I will return as the Fire Keeper I once was."
                    # talk:12001003:"As it always has been."
                    assert t400120_x6(text1=12001000, flag1=0, mode1=0)
                else:
                    """State 11,26"""
                    # talk:12001900:"Ashen one, forgive me if this soundeth strange."
                    # talk:12001901:"The eyes show a world without fire, a vast stretch of darkness."
                    # talk:12001902:"But 'tis different to what is seen when stripped of vision."
                    # talk:12001903:"In the far distance, I sense the presence of tiny flames."
                    # talk:12001904:"Like precious embers, left to us by past Lords, linkers of the fire."
                    # talk:12001905:"Could this be what draws me to this strangely enticing darkness?"
                    assert t400120_x5(text2=12001900, flag2=74000110, flag3=0, mode2=0)
            else:
                """State 9,22"""
                # talk:12001200:"Ashen one, kill me, and take these eyes away."
                # talk:12001201:"Before I am drawn into the darkness."
                # talk:12001202:"Seduced by the thin light, and the awful betrayal..."
                assert t400120_x6(text1=12001200, flag1=0, mode1=0)
    """State 27"""
    return 0

def t400120_x21(goods1=2138):
    """State 0,6"""
    # action:12002000:"Give <?gdsparam@2138?>?"
    call = t400120_x0(action2=12002000)
    if call.Get() == 0:
        """State 2,1"""
        # goods:2138:Eyes of a Fire Keeper
        PlayerEquipmentQuantityChange(ItemType.Goods, goods1, -1)
        """State 3"""
        SetEventFlag(50006020, FlagState.Off)
        """State 5"""
        SetEventFlag(74000122, FlagState.On)
        """State 7"""
        # talk:12003300:"...Ashen one, are these..."
        # talk:12003301:"...are these eyes?"
        # talk:12003302:"How gracious of thee, ashen one."
        # talk:12003303:"The very things we Fire Keepers have been missing..."
        assert t400120_x6(text1=12003300, flag1=0, mode1=0)
    elif call.Done():
        """State 4"""
        pass
    """State 8"""
    return 0

def t400120_x22(goods2=390):
    """State 0,5"""
    # action:12002001:"Give <?gdsparam@390?>?"
    call = t400120_x0(action2=12002001)
    if call.Get() == 0:
        """State 2,1"""
        # goods:390:Fire Keeper Soul
        PlayerEquipmentQuantityChange(ItemType.Goods, goods2, -1)
        """State 3"""
        SetEventFlag(74000125, FlagState.On)
        """State 6"""
        # talk:12003400:"...Ashen one, this is..."
        # talk:12003401:"...much like what lies within me..."
        # talk:12003402:"Then let it find its own place, within my bosom."
        # talk:12003403:"She will understand. We are both Fire Keepers, after all."
        assert (t400120_x6(text1=12003400, flag1=0, mode1=0) and (not CheckSpecificPersonGenericDialogIsOpen(2)
                and not (CheckSpecificPersonMenuIsOpen(-1, 2) and not CheckSpecificPersonGenericDialogIsOpen(2))))
        """State 7"""
        # action:13002030:"The Fire Keeper is now able to heal the dark sigil"
        assert t400120_x7(action1=13002030)
        """State 8"""
        # talk:12003500:"Forgive me, sister."
        # talk:12003501:"May the flames guide thy way."
        assert t400120_x6(text1=12003500, flag1=0, mode1=0)
    elif call.Done():
        """State 4"""
        pass
    """State 9"""
    return 0

def t400120_x23(goods3=490, z1=0):
    """State 0,1"""
    # goods:490:Dark Sigil
    if ComparePlayerInventoryNumber(ItemType.Goods, goods3, CompareType.Equal, 0, False):
        """State 3,20"""
        # action:13002021:"You have no dark sigil"
        assert t400120_x7(action1=13002021)
    else:
        """State 2,24"""
        assert t400120_x24(goods3=goods3, z1=z1)
        """State 10"""
        SetMessageTagValue(0, GetLevelUpSoulCost(GetStatus(PlayerStat.SoulLevel), GetStatus(PlayerStat.SoulLevel) + GetWorkValue(z1)))
        """State 21"""
        # action:12002002:"Requires <?evntAcquittalPrice?> souls. \nWill you choose to heal the dark sigil?"
        call = t400120_x0(action2=12002002)
        if call.Get() == 0:
            """State 6"""
            if (ComparePlayerStat(PlayerStat.SoulsCollected, CompareType.Greater, GetLevelUpSoulCost(GetStatus(PlayerStat.SoulLevel),
                GetStatus(PlayerStat.SoulLevel) + GetWorkValue(z1)))):
                """State 4,13"""
                TurnCharacterToFaceEntity(-1, 10000, -1)
                assert GetCurrentStateElapsedFrames() > 1 and GetWhetherChrEventAnimHasEnded(10000)
                """State 12"""
                TurnCharacterToFaceEntity(69010, 10000, -1)
                assert GetCurrentStateElapsedTime() > 1.5
                """State 8"""
                # goods:490:Dark Sigil
                PlayerEquipmentQuantityChange(ItemType.Goods, goods3, -1 * GetWorkValue(z1))
                """State 9"""
                ChangePlayerStat(PlayerStat.SoulsCollected, ChangeType.Subtract, GetLevelUpSoulCost(GetStatus(PlayerStat.SoulLevel), GetStatus(PlayerStat.SoulLevel) + GetWorkValue(z1)))
                """State 11"""
                SetEventFlag(74000124, FlagState.On)
                """State 14"""
                if GetPlayerChrType() == ChrType.Hollow:
                    """State 15,18"""
                    GiveSpEffectToPlayer(3093)
                else:
                    """State 16,17"""
                    ChangePlayerStat(PlayerStat.Hollowing, ChangeType.Set, 0)
                """State 19"""
                assert GetCurrentStateElapsedTime() > 3
                """State 23"""
                # action:13002020:"Dark sigil has been healed"
                assert t400120_x7(action1=13002020) and GetWhetherChrEventAnimHasEnded(10000)
            else:
                """State 5,22"""
                # action:13000050:"Insufficient souls"
                assert t400120_x7(action1=13000050)
        elif call.Done():
            """State 7"""
            pass
    """State 25"""
    return 0

def t400120_x24(goods3=490, z1=0):
    """State 0,1"""
    # goods:490:Dark Sigil
    SetWorkValue(z1, GetItemHeldNumLimit(ItemType.Goods, goods3))
    while True:
        """State 5"""
        # goods:490:Dark Sigil
        if (ComparePlayerInventoryNumber(ItemType.Goods, goods3, CompareType.Equal, GetWorkValue(z1), False) or
            GetWorkValue(z1) <= 0):
            break
        else:
            """State 3,2"""
            SetWorkValue(z1, GetWorkValue(z1) - 1)
    """State 4,6"""
    return 0

def t400120_x25():
    """State 0,3"""
    if DoesSelfHaveSpEffect(150) or DoesSelfHaveSpEffect(152):
        """State 4"""
        SetEventFlag(74000136, FlagState.On)
        """State 2"""
        if not GetEventFlag(74000135):
            pass
        elif GetEventFlag(74000137) and GetEventFlag(74000138):
            """State 1"""
            OpenSoul()
            assert not (CheckSpecificPersonMenuIsOpen(10, 0) and not CheckSpecificPersonGenericDialogIsOpen(0))
            """State 5"""
            return 0
    elif not GetEventFlag(74000135):
        pass
    """State 6"""
    return 1

def t400120_x26():
    """State 0"""
    while True:
        """State 5"""
        call = t400120_x1(actionbutton1=6120, flag6=1015, flag7=6000, flag8=6000, flag9=6000, flag10=6000)
        if call.Done():
            """State 3"""
            SetEventFlag(74000139, FlagState.On)
            call = t400120_x9()
            if call.Done():
                pass
            elif IsAttackedBySomeone():
                """State 1"""
                Label('L0')
                call = t400120_x10()
                def ExitPause():
                    RemoveMyAggro()
                if call.Done():
                    pass
                elif IsPlayerDead():
                    break
            elif IsPlayerDead():
                break
            elif GetDistanceToPlayer() > 3 or GetPlayerYDistance() > 0.25:
                """State 4"""
                call = t400120_x13()
                if call.Done() and (GetDistanceToPlayer() < 2.5 and GetPlayerYDistance() < 0.249):
                    pass
                elif IsAttackedBySomeone():
                    Goto('L0')
        elif IsAttackedBySomeone():
            Goto('L0')
        elif IsPlayerDead():
            break
    """State 2"""
    t400120_x12()
    Quit()
    """Unused"""
    """State 6"""
    return 0
