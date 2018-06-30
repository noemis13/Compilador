; ModuleID = "Programa"
target triple = "unknown-unknown-unknown"
target datalayout = ""

declare float @"escrevaFlutuante"(float %".1") 

declare i32 @"escrevaInteiro"(i32 %".1") 

declare float @"leiaFlutuante"() 

declare i32 @"leiaInteiro"() 

@"global.a" = external global i32
define i32 @"main"() 
{
entry:
  %"principal.ret" = alloca i32
  %".2" = fptosi float 0x4024000000000000 to i32
  store i32 %".2", i32* @"global.a"
  %".4" = load i32, i32* @"global.a"
  %".5" = sitofp i32 %".4" to float
  %".6" = load i32, i32* @"global.a"
  %".7" = sitofp i32 %".6" to float
  %"fcmpMaior" = fcmp ugt float %".7", 0x4014000000000000
  br i1 %"fcmpMaior", label %"entao", label %"senao"
entao:
  %".9" = fptosi float 0x3ff0000000000000 to i32
  store i32 %".9", i32* %"principal.ret"
  %".11" = load i32, i32* %"principal.ret"
  %".12" = sitofp i32 %".11" to float
  br label %"fim"
senao:
  %".14" = fptosi float              0x0 to i32
  store i32 %".14", i32* %"principal.ret"
  %".16" = load i32, i32* %"principal.ret"
  %".17" = sitofp i32 %".16" to float
  br label %"fim"
fim:
  %"seTmp" = phi float [%".12", %"entao"], [%".17", %"senao"]
  %".19" = fptosi float              0x0 to i32
  ret i32 %".19"
}
