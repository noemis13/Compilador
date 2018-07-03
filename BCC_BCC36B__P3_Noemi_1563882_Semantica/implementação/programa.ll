; ModuleID = "Programa"
target triple = "unknown-unknown-unknown"
target datalayout = ""

declare float @"escrevaFlutuante"(float %".1") 

declare i32 @"escrevaInteiro"(i32 %".1") 

declare float @"leiaFlutuante"() 

declare i32 @"leiaInteiro"() 

@"global.n" = external global i32
@"global.soma" = external global i32
@"global.a" = external global i32
@"global.b" = external global i32
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
  %".11" = load i32, i32* @"global.n"
  %".12" = sitofp i32 %".11" to float
  %".13" = fptosi float %".12" to i32
  store i32 %".13", i32* @"global.a"
  %".15" = load i32, i32* @"global.a"
  %".16" = sitofp i32 %".15" to float
  %".17" = fptosi float 0x3ff0000000000000 to i32
  store i32 %".17", i32* @"global.n"
  %".19" = load i32, i32* @"global.n"
  %".20" = sitofp i32 %".19" to float
  %".21" = load i32, i32* @"global.n"
  %".22" = sitofp i32 %".21" to float
  %"fcmpIgual" = fcmp ueq float %".22",              0x0
  br i1 %"fcmpIgual", label %"repita", label %"fimRepita"
fimRepita:
  %"repitaTmp" = phi i32 [%".20", %"repita"]
  %".24" = fptosi float              0x0 to i32
  ret i32 %".24"
}
