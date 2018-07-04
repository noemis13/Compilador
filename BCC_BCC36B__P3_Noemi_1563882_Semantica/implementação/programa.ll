; ModuleID = "Programa"
target triple = "unknown-unknown-unknown"
target datalayout = ""

declare float @"escrevaFlutuante"(float %".1") 

declare i32 @"escrevaInteiro"(i32 %".1") 

declare float @"leiaFlutuante"() 

declare i32 @"leiaInteiro"() 

@"global.n" = external global i32
@"global.soma" = external global i32
define i32 @"main"() 
{
entry:
  %".2" = fptosi float 0x4024000000000000 to i32
  store i32 %".2", i32* @"global.n"
  %".4" = load i32, i32* @"global.n"
  %".5" = sitofp i32 %".4" to float
  %".6" = fptosi float              0x0 to i32
  store i32 %".6", i32* @"global.soma"
  %".8" = load i32, i32* @"global.soma"
  %".9" = sitofp i32 %".8" to float
  br label %"repita"
repita:
  %".11" = load i32, i32* @"global.soma"
  %".12" = sitofp i32 %".11" to float
  %".13" = load i32, i32* @"global.n"
  %".14" = sitofp i32 %".13" to float
  %"addtmp" = fadd float %".12", %".14"
  %".15" = fptosi float %"addtmp" to i32
  store i32 %".15", i32* @"global.soma"
  %".17" = load i32, i32* @"global.soma"
  %".18" = sitofp i32 %".17" to float
  %".19" = fptosi float 0x3ff0000000000000 to i32
  store i32 %".19", i32* @"global.n"
  %".21" = load i32, i32* @"global.n"
  %".22" = sitofp i32 %".21" to float
  %".23" = load i32, i32* @"global.n"
  %".24" = sitofp i32 %".23" to float
  %"fcmpIgual" = fcmp ueq float %".24",              0x0
  br i1 %"fcmpIgual", label %"repita", label %"fimRepita"
fimRepita:
  %"repitaTmp" = phi i32 [%".22", %"repita"]
  %".26" = load i32, i32* @"global.soma"
  %".27" = sitofp i32 %".26" to float
  %".28" = call float @"escrevaFlutuante"(float %".27")
  %".29" = fptosi float              0x0 to i32
  ret i32 %".29"
}
