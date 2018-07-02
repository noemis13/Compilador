; ModuleID = "ModuloLLVMLITE.bc"
target triple = "unknown-unknown-unknown"
target datalayout = ""

declare float @"escrevaFlutuante"(float %".1") 

declare i32 @"escrevaInteiro"(i32 %".1") 

declare float @"leiaFlutuante"() 

declare i32 @"leiaInteiro"() 

@"a" = common global i32 0, align 4
define i32 @"main"() 
{
entry:
  %"principal-ret" = alloca i32
  store i32 10, i32* @"a"
  %"a_cmp" = load i32, i32* @"a", align 4
  %"se_a" = icmp sgt i32 %"a_cmp", 5
  br i1 %"se_a", label %"entao", label %"senao"
entao:
  store i32 1, i32* %"principal-ret"
  br label %"fim"
senao:
  store i32 10, i32* %"principal-ret"
  br label %"fim"
fim:
  ret i32 10
}
