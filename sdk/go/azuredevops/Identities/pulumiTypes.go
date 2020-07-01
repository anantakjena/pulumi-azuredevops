// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package Identities

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

type GetUsersUser struct {
	Descriptor    string  `pulumi:"descriptor"`
	DisplayName   string  `pulumi:"displayName"`
	MailAddress   string  `pulumi:"mailAddress"`
	Origin        string  `pulumi:"origin"`
	OriginId      *string `pulumi:"originId"`
	PrincipalName string  `pulumi:"principalName"`
}

// GetUsersUserInput is an input type that accepts GetUsersUserArgs and GetUsersUserOutput values.
// You can construct a concrete instance of `GetUsersUserInput` via:
//
//          GetUsersUserArgs{...}
type GetUsersUserInput interface {
	pulumi.Input

	ToGetUsersUserOutput() GetUsersUserOutput
	ToGetUsersUserOutputWithContext(context.Context) GetUsersUserOutput
}

type GetUsersUserArgs struct {
	Descriptor    pulumi.StringInput    `pulumi:"descriptor"`
	DisplayName   pulumi.StringInput    `pulumi:"displayName"`
	MailAddress   pulumi.StringInput    `pulumi:"mailAddress"`
	Origin        pulumi.StringInput    `pulumi:"origin"`
	OriginId      pulumi.StringPtrInput `pulumi:"originId"`
	PrincipalName pulumi.StringInput    `pulumi:"principalName"`
}

func (GetUsersUserArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetUsersUser)(nil)).Elem()
}

func (i GetUsersUserArgs) ToGetUsersUserOutput() GetUsersUserOutput {
	return i.ToGetUsersUserOutputWithContext(context.Background())
}

func (i GetUsersUserArgs) ToGetUsersUserOutputWithContext(ctx context.Context) GetUsersUserOutput {
	return pulumi.ToOutputWithContext(ctx, i).(GetUsersUserOutput)
}

// GetUsersUserArrayInput is an input type that accepts GetUsersUserArray and GetUsersUserArrayOutput values.
// You can construct a concrete instance of `GetUsersUserArrayInput` via:
//
//          GetUsersUserArray{ GetUsersUserArgs{...} }
type GetUsersUserArrayInput interface {
	pulumi.Input

	ToGetUsersUserArrayOutput() GetUsersUserArrayOutput
	ToGetUsersUserArrayOutputWithContext(context.Context) GetUsersUserArrayOutput
}

type GetUsersUserArray []GetUsersUserInput

func (GetUsersUserArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]GetUsersUser)(nil)).Elem()
}

func (i GetUsersUserArray) ToGetUsersUserArrayOutput() GetUsersUserArrayOutput {
	return i.ToGetUsersUserArrayOutputWithContext(context.Background())
}

func (i GetUsersUserArray) ToGetUsersUserArrayOutputWithContext(ctx context.Context) GetUsersUserArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(GetUsersUserArrayOutput)
}

type GetUsersUserOutput struct{ *pulumi.OutputState }

func (GetUsersUserOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetUsersUser)(nil)).Elem()
}

func (o GetUsersUserOutput) ToGetUsersUserOutput() GetUsersUserOutput {
	return o
}

func (o GetUsersUserOutput) ToGetUsersUserOutputWithContext(ctx context.Context) GetUsersUserOutput {
	return o
}

func (o GetUsersUserOutput) Descriptor() pulumi.StringOutput {
	return o.ApplyT(func(v GetUsersUser) string { return v.Descriptor }).(pulumi.StringOutput)
}

func (o GetUsersUserOutput) DisplayName() pulumi.StringOutput {
	return o.ApplyT(func(v GetUsersUser) string { return v.DisplayName }).(pulumi.StringOutput)
}

func (o GetUsersUserOutput) MailAddress() pulumi.StringOutput {
	return o.ApplyT(func(v GetUsersUser) string { return v.MailAddress }).(pulumi.StringOutput)
}

func (o GetUsersUserOutput) Origin() pulumi.StringOutput {
	return o.ApplyT(func(v GetUsersUser) string { return v.Origin }).(pulumi.StringOutput)
}

func (o GetUsersUserOutput) OriginId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetUsersUser) *string { return v.OriginId }).(pulumi.StringPtrOutput)
}

func (o GetUsersUserOutput) PrincipalName() pulumi.StringOutput {
	return o.ApplyT(func(v GetUsersUser) string { return v.PrincipalName }).(pulumi.StringOutput)
}

type GetUsersUserArrayOutput struct{ *pulumi.OutputState }

func (GetUsersUserArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]GetUsersUser)(nil)).Elem()
}

func (o GetUsersUserArrayOutput) ToGetUsersUserArrayOutput() GetUsersUserArrayOutput {
	return o
}

func (o GetUsersUserArrayOutput) ToGetUsersUserArrayOutputWithContext(ctx context.Context) GetUsersUserArrayOutput {
	return o
}

func (o GetUsersUserArrayOutput) Index(i pulumi.IntInput) GetUsersUserOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) GetUsersUser {
		return vs[0].([]GetUsersUser)[vs[1].(int)]
	}).(GetUsersUserOutput)
}

func init() {
	pulumi.RegisterOutputType(GetUsersUserOutput{})
	pulumi.RegisterOutputType(GetUsersUserArrayOutput{})
}
