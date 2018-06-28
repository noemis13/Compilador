; ModuleID = "Programa"
target datalayout = ""

declare float @"escrevaFlutuante"(float %".1") 

declare i32 @"escrevaInteiro"(i32 %".1") 

declare float @"leiaFlutuante"() 

declare i32 @"leiaInteiro"() 

@"global.a" = external global i32
define i32 @"main"() 
{
entry:
  %"principal.b" = alloca i32
  %".2" = fptosi float 0x4024000000000000 to i32
  store i32 %".2", i32* @"global.a"
  %".4" = load i32, i32* @"global.a"
  %".5" = sitofp i32 %".4" to float
  %".6" = load i32, i32* @"global.a"
  %".7" = sitofp i32 %".6" to float
  %".8" = fptosi float %".7" to i32
  store i32 %".8", i32* %"principal.b"
  %".10" = load i32, i32* %"principal.b"
  %".11" = sitofp i32 %".10" to float
  %".12" = fptosi float              0x0 to i32
  ret i32 %".12"
}

