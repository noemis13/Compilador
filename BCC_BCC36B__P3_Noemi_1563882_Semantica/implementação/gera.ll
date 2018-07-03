; ModuleID = "ModuloLLVMLITE.bc"
target triple = "unknown-unknown-unknown"
target datalayout = ""

declare float @"escrevaFlutuante"(float %".1") 

declare i32 @"escrevaInteiro"(i32 %".1") 

declare float @"leiaFlutuante"() 

declare i32 @"leiaInteiro"() 

@"n" = common global i32 0, align 4
@"soma" = common global i32 0, align 4
@"a" = common global i32 0, align 4
@"b" = common global i32 0, align 4
define i32 @"main"() 
{
entry:
  store i32 10, i32* @"n"
  store i32 0, i32* @"soma"
  br label %"repita"
repita:
  %"global-soma" = load i32, i32* @"n"
  store i32 %"global-soma", i32* @"soma"
  %".6" = load i32, i32* @"n"
  store i32 1, i32* @"n"
  %".8" = load i32, i32* @"n"
  %"n_cmp" = load i32, i32* @"n", align 4
  %"Igualdade" = icmp eq i32 %"n_cmp", 0
  br i1 %"Igualdade", label %"repita", label %"fim"
fim:
  %"repitaTemp" = phi i32 [%".8", %"repita"]
  %".10" = load i32, i32* @"n"
  %".11" = sitofp i32 %".10" to float
  %".12" = call float @"escrevaFlutuante"(float %".11")
  ret i32 0
}
