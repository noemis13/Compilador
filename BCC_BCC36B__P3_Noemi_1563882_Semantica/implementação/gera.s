	.text
	.file	"gera.ll"
	.globl	soma                    # -- Begin function soma
	.p2align	4, 0x90
	.type	soma,@function
soma:                                   # @soma
	.cfi_startproc
# BB#0:                                 # %entry
                                        # kill: %EDI<def> %EDI<kill> %RDI<def>
	movl	%edi, -12(%rsp)
	movl	%esi, -16(%rsp)
	leal	(%rdi,%rdi), %eax
	retq
.Lfunc_end0:
	.size	soma, .Lfunc_end0-soma
	.cfi_endproc
                                        # -- End function
	.globl	main                    # -- Begin function main
	.p2align	4, 0x90
	.type	main,@function
main:                                   # @main
	.cfi_startproc
# BB#0:                                 # %entry
	subq	$24, %rsp
.Lcfi0:
	.cfi_def_cfa_offset 32
	callq	leiaFlutuante
	cvttss2si	%xmm0, %eax
	movl	%eax, 12(%rsp)
	callq	leiaFlutuante
	cvttss2si	%xmm0, %eax
	movl	%eax, 20(%rsp)
	cvtsi2ssl	12(%rsp), %xmm0
	cvtsi2ssl	%eax, %xmm1
	cvttss2si	%xmm0, %edi
	cvttss2si	%xmm1, %esi
	callq	soma
	xorps	%xmm0, %xmm0
	cvtsi2ssl	16(%rsp), %xmm0
	callq	escrevaFlutuante
	xorl	%eax, %eax
	addq	$24, %rsp
	retq
.Lfunc_end1:
	.size	main, .Lfunc_end1-main
	.cfi_endproc
                                        # -- End function

	.section	".note.GNU-stack","",@progbits
