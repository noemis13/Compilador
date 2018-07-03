	.text
	.file	"programa.ll"
	.globl	soma                    # -- Begin function soma
	.p2align	4, 0x90
	.type	soma,@function
soma:                                   # @soma
	.cfi_startproc
# BB#0:                                 # %entry
	movl	%edi, -4(%rsp)
	movl	%esi, -8(%rsp)
	xorl	%eax, %eax
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
	movl	%eax, 16(%rsp)
	callq	leiaFlutuante
	cvttss2si	%xmm0, %eax
	movl	%eax, 12(%rsp)
	xorl	%eax, %eax
	addq	$24, %rsp
	retq
.Lfunc_end1:
	.size	main, .Lfunc_end1-main
	.cfi_endproc
                                        # -- End function

	.section	".note.GNU-stack","",@progbits
