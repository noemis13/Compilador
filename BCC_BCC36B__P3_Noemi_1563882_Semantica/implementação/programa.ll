; ModuleID = "Programa"
target triple = "unknown-unknown-unknown"
target datalayout = ""

declare float @"escrevaFlutuante"(float %".1") 

declare i32 @"escrevaInteiro"(i32 %".1") 

declare float @"leiaFlutuante"() 

declare i32 @"leiaInteiro"() 

define i32 @"main"() 
{
entry:
  %"principal.a" = alloca i32
  %"principal.b" = alloca i32
  %"principal.c" = alloca i32
  %"leiaFlutuante" = call float @"leiaFlutuante"()
  %".2" = fptosi float %"leiaFlutuante" to i32
  store i32 %".2", i32* %"principal.a"
  %".4" = load i32, i32* %"principal.a"
  %"leiaFlutuante.1" = call float @"leiaFlutuante"()
  %".5" = fptosi float %"leiaFlutuante.1" to i32
  store i32 %".5", i32* %"principal.b"
  %".7" = load i32, i32* %"principal.b"
  %".8" = load i32, i32* %"principal.a"
  %".9" = sitofp i32 %".8" to float
  %".10" = call float @"escrevaFlutuante"(float %".9")
  %".11" = load i32, i32* %"principal.a"
  %".12" = sitofp i32 %".11" to float
  %".13" = load i32, i32* %"principal.b"
  %".14" = sitofp i32 %".13" to float
  %"addtmp" = fadd float %".12", %".14"
  %".15" = fptosi float %"addtmp" to i32
  ret i32 %".15"
}
